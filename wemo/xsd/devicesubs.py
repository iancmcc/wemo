#!/usr/bin/env python

#
# Generated Thu Jan 31 15:50:44 2013 by generateDS.py version 2.8b.
#

import sys

import ??? as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#

class rootSub(supermod.root):
    def __init__(self, specVersion=None, URLBase=None, device=None):
        super(rootSub, self).__init__(specVersion, URLBase, device, )
supermod.root.subclass = rootSub
# end class rootSub


class SpecVersionTypeSub(supermod.SpecVersionType):
    def __init__(self, major=None, minor=None):
        super(SpecVersionTypeSub, self).__init__(major, minor, )
supermod.SpecVersionType.subclass = SpecVersionTypeSub
# end class SpecVersionTypeSub


class DeviceTypeSub(supermod.DeviceType):
    def __init__(self, deviceType=None, friendlyName=None, manufacturer=None, manufacturerURL=None, modelDescription=None, modelName=None, modelNumber=None, modelURL=None, serialNumber=None, UDN=None, UPC=None, iconList=None, serviceList=None, deviceList=None, presentationURL=None, anytypeobjs_=None):
        super(DeviceTypeSub, self).__init__(deviceType, friendlyName, manufacturer, manufacturerURL, modelDescription, modelName, modelNumber, modelURL, serialNumber, UDN, UPC, iconList, serviceList, deviceList, presentationURL, anytypeobjs_, )
supermod.DeviceType.subclass = DeviceTypeSub
# end class DeviceTypeSub


class IconListTypeSub(supermod.IconListType):
    def __init__(self, icon=None):
        super(IconListTypeSub, self).__init__(icon, )
supermod.IconListType.subclass = IconListTypeSub
# end class IconListTypeSub


class ServiceListTypeSub(supermod.ServiceListType):
    def __init__(self, service=None):
        super(ServiceListTypeSub, self).__init__(service, )
supermod.ServiceListType.subclass = ServiceListTypeSub
# end class ServiceListTypeSub


class DeviceListTypeSub(supermod.DeviceListType):
    def __init__(self, device=None):
        super(DeviceListTypeSub, self).__init__(device, )
supermod.DeviceListType.subclass = DeviceListTypeSub
# end class DeviceListTypeSub


class iconTypeSub(supermod.iconType):
    def __init__(self, mimetype=None, width=None, height=None, depth=None, url=None):
        super(iconTypeSub, self).__init__(mimetype, width, height, depth, url, )
supermod.iconType.subclass = iconTypeSub
# end class iconTypeSub


class serviceTypeSub(supermod.serviceType):
    def __init__(self, serviceType=None, serviceId=None, SCPDURL=None, controlURL=None, eventSubURL=None):
        super(serviceTypeSub, self).__init__(serviceType, serviceId, SCPDURL, controlURL, eventSubURL, )
supermod.serviceType.subclass = serviceTypeSub
# end class serviceTypeSub



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'root'
        rootClass = supermod.root
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    doc = None
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'root'
        rootClass = supermod.root
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'root'
        rootClass = supermod.root
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from ??? import *\n\n')
    sys.stdout.write('import ??? as model_\n\n')
    sys.stdout.write('rootObj = model_.root(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="root")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


