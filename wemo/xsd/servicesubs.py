#!/usr/bin/env python

#
# Generated Thu Jan 31 15:52:45 2013 by generateDS.py version 2.8b.
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

class scpdSub(supermod.scpd):
    def __init__(self, specVersion=None, actionList=None, serviceStateTable=None):
        super(scpdSub, self).__init__(specVersion, actionList, serviceStateTable, )
supermod.scpd.subclass = scpdSub
# end class scpdSub


class SpecVersionTypeSub(supermod.SpecVersionType):
    def __init__(self, major=None, minor=None):
        super(SpecVersionTypeSub, self).__init__(major, minor, )
supermod.SpecVersionType.subclass = SpecVersionTypeSub
# end class SpecVersionTypeSub


class ActionListTypeSub(supermod.ActionListType):
    def __init__(self, action=None):
        super(ActionListTypeSub, self).__init__(action, )
supermod.ActionListType.subclass = ActionListTypeSub
# end class ActionListTypeSub


class ActionTypeSub(supermod.ActionType):
    def __init__(self, name=None, argumentList=None):
        super(ActionTypeSub, self).__init__(name, argumentList, )
supermod.ActionType.subclass = ActionTypeSub
# end class ActionTypeSub


class ArgumentListTypeSub(supermod.ArgumentListType):
    def __init__(self, argument=None):
        super(ArgumentListTypeSub, self).__init__(argument, )
supermod.ArgumentListType.subclass = ArgumentListTypeSub
# end class ArgumentListTypeSub


class ArgumentTypeSub(supermod.ArgumentType):
    def __init__(self, name=None, direction=None, relatedStateVariable=None, retval=None):
        super(ArgumentTypeSub, self).__init__(name, direction, relatedStateVariable, retval, )
supermod.ArgumentType.subclass = ArgumentTypeSub
# end class ArgumentTypeSub


class ServiceStateTableTypeSub(supermod.ServiceStateTableType):
    def __init__(self, stateVariable=None):
        super(ServiceStateTableTypeSub, self).__init__(stateVariable, )
supermod.ServiceStateTableType.subclass = ServiceStateTableTypeSub
# end class ServiceStateTableTypeSub


class StateVariableTypeSub(supermod.StateVariableType):
    def __init__(self, sendEvents='yes', name=None, dataType=None, defaultValue=None, allowedValueList=None, allowedValueRange=None):
        super(StateVariableTypeSub, self).__init__(sendEvents, name, dataType, defaultValue, allowedValueList, allowedValueRange, )
supermod.StateVariableType.subclass = StateVariableTypeSub
# end class StateVariableTypeSub


class AllowedValueListTypeSub(supermod.AllowedValueListType):
    def __init__(self, allowedValue=None):
        super(AllowedValueListTypeSub, self).__init__(allowedValue, )
supermod.AllowedValueListType.subclass = AllowedValueListTypeSub
# end class AllowedValueListTypeSub


class AllowedValueRangeTypeSub(supermod.AllowedValueRangeType):
    def __init__(self, minimum=None, maximum=None, step=None):
        super(AllowedValueRangeTypeSub, self).__init__(minimum, maximum, step, )
supermod.AllowedValueRangeType.subclass = AllowedValueRangeTypeSub
# end class AllowedValueRangeTypeSub


class retvalTypeSub(supermod.retvalType):
    def __init__(self):
        super(retvalTypeSub, self).__init__()
supermod.retvalType.subclass = retvalTypeSub
# end class retvalTypeSub



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
        rootTag = 'scpd'
        rootClass = supermod.scpd
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
        rootTag = 'scpd'
        rootClass = supermod.scpd
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
        rootTag = 'scpd'
        rootClass = supermod.scpd
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from ??? import *\n\n')
    sys.stdout.write('import ??? as model_\n\n')
    sys.stdout.write('rootObj = model_.scpd(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="scpd")
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


