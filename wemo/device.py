from xml.etree import cElementTree as et
from gevent import monkey

monkey.patch_socket()
import requests

from wemo.xsd import device as deviceParser, service as serviceParser
from wemo.xsd import envelope as envelopeParser


REQUEST_TEMPLATE = """
<?xml version="1.0" encoding="utf-8"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
 <s:Body>
  <u:{action} xmlns:u="{service}">
   {args}
  </u:{action}>
 </s:Body>
</s:Envelope>
"""

class WemoService(object):
    def __init__(self, service, base_url):
        self._base_url = base_url.rstrip('/')
        self._config = service
        url = '%s/%s' % (base_url, service.get_SCPDURL().strip('/'))
        xml = requests.get(url)
        self._svc_config = serviceParser.parseString(xml.content).actionList
        self.actions = {a.get_name(): a for a in self._svc_config.get_action()}

    @property
    def hostname(self):
        return self._base_url.split('/')[-1]

    @property
    def controlURL(self):
        return '%s/%s' % (self._base_url, self._config.get_controlURL().strip('/'))

    @property
    def serviceType(self):
        return self._config.get_serviceType()

    def __getattr__(self, attr):
        if attr not in self.actions:
            raise AttributeError(attr)

        def _act(**kwargs):
            arglist = '\n'.join('<{0}>{1}</{0}>'.format(arg, value) for arg, value in kwargs.iteritems())
            body = REQUEST_TEMPLATE.format(
                action=attr,
                service=self.serviceType,
                args=arglist
            )
            headers = {
                'Content-Type': 'text/xml',
                'SOAPACTION': '"%s#%s"' % (self.serviceType, attr)
            }
            response = requests.post(self.controlURL, body.strip(), headers=headers)
            d = {}
            for r in et.fromstring(response.content).getchildren()[0].getchildren()[0].getchildren():
                d[r.tag] = r.text
            return d

        _act.__name__ = attr
        return _act


class WemoDevice(object):
    def __init__(self, url):
        base_url = url.rsplit('/', 1)[0]
        xml = requests.get(url)
        self._config = deviceParser.parseString(xml.content).device
        sl = self._config.serviceList
        self.services = {}
        for svc in sl.service:
            svcname = svc.get_serviceType().split(':')[-2]
            self.services[svcname] = WemoService(svc, base_url)

    def get_service(self, name):
        return self.services.get(name, None)

    @property
    def model(self):
        return self._config.get_modelDescription()

    @property
    def name(self):
        return self._config.get_friendlyName()

    @property
    def serialnumber(self):
        return self._config.get_serialNumber()


if __name__ == "__main__":
    device = WemoDevice("http://10.42.1.102:49152/setup.xml")
    print device.get_service('basicevent').SetBinaryState(BinaryState=0)

