import xml.etree.cElementTree as et

import gevent
from gevent import monkey; monkey.patch_socket()
import requests


REQUEST_TEMPLATE =  """
<?xml version="1.0" encoding="utf-8"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
 <s:Body>
  <u:{action} xmlns:u="{service}">
   {args}
  </u:{action}>
 </s:Body>
</s:Envelope>
"""


class WemoDevice(object):
    """
    Base class for a WeMo device (switch or motion)
    """
    _NS = '{urn:Belkin:device-1-0}'

    def __init__(self, url):
        self._url_root = url.rsplit('/', 1)[0]
        et.register_namespace(self._NS, '')

        xml = requests.get(url)
        self._doc = et.fromstring(xml.content)
        self.name = self._text('/device/friendlyName')
        self.description = self._text('/device/modelDescription')

        self.services = {}
        for service in self._find('/device/serviceList/service'):
            d = {}
            for attr in ('serviceType', 'serviceId', 'controlURL', 'eventSubURL', 'SCPDURL'):
                d[attr] = self._text('/' + attr, service)
            gevent.spawn(self._get_service, d)

    def _text(self, xpath, root=None):
        return self._find(xpath, root)[0].text

    def _find(self, xpath, root=None):
        newpath = '/{ns}'.format(ns=self._NS).join(xpath.split('/'))
        return (root or self._doc).findall('.' + newpath)

    def _get_service(self, service_dict):
        svcurl = '%s/%s' % (self._url_root, service_dict['SCPDURL'])
        xml = requests.get(svcurl)
        doc = et.fromstring(xml.content)
        for action in doc.findall('.//{urn:Belkin:service-1-0}action'):
            a = {}
            a['name'] = action.find('./name').text
        self.services[service_dict['serviceType']] = service_dict


if __name__ == "__main__":
    device = WemoDevice("http://10.42.1.102:49152/setup.xml")
    gevent.sleep(10)
