import unittest

import Zope # Sigh, make product initialization happen

try:
    Zope.startup()
except: # Zope > 2.6
    pass

from Products.Archetypes.Field import *
from Products.PortalTransforms.MimeTypesRegistry import MimeTypesRegistry
from Products.Archetypes.BaseUnit import BaseUnit

class SiteProperties:
    default_charset = 'UTF-8'
    def getProperty(self, name, default=None):
        return getattr(self, name, default)
    
class PortalProperties:
    site_properties = SiteProperties()

registry = MimeTypesRegistry()
registry.portal_properties = PortalProperties()
BaseUnit.portal_properties = PortalProperties()

class Dummy:
    portal_properties = PortalProperties()
    mimetypes_registry = registry
    
instance = Dummy()

class UnicodeStringFieldTest( unittest.TestCase ):
    
    def test_set(self):
        f = StringField('test')
        f.set(instance, 'h\xc3\xa9h\xc3\xa9h\xc3\xa9')
        self.failUnlessEqual(f.get(instance), 'h\xc3\xa9h\xc3\xa9h\xc3\xa9')
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), 'h�h�h�')
        f.set(instance, 'h�h�h�', encoding='ISO-8859-1')
        self.failUnlessEqual(f.get(instance), 'h\xc3\xa9h\xc3\xa9h\xc3\xa9')
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), 'h�h�h�')
        f.set(instance, u'h�h�h�')
        self.failUnlessEqual(f.get(instance), 'h\xc3\xa9h\xc3\xa9h\xc3\xa9')
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), 'h�h�h�')
            
class UnicodeLinesFieldTest( unittest.TestCase ):
    
    def test_set1(self):
        f = LinesField('test')
        f.set(instance, 'h\xc3\xa9h\xc3\xa9h\xc3\xa9')
        self.failUnlessEqual(f.get(instance), ['h\xc3\xa9h\xc3\xa9h\xc3\xa9'])
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), ['h�h�h�'])
        f.set(instance, 'h�h�h�', encoding='ISO-8859-1')
        self.failUnlessEqual(f.get(instance), ['h\xc3\xa9h\xc3\xa9h\xc3\xa9'])
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), ['h�h�h�'])
        f.set(instance, u'h�h�h�')
        self.failUnlessEqual(f.get(instance), ['h\xc3\xa9h\xc3\xa9h\xc3\xa9'])
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), ['h�h�h�'])

    def test_set2(self):
        f = LinesField('test')
        f.set(instance, ['h\xc3\xa9h\xc3\xa9h\xc3\xa9'])
        self.failUnlessEqual(f.get(instance), ['h\xc3\xa9h\xc3\xa9h\xc3\xa9'])
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), ['h�h�h�'])
        f.set(instance, ['h�h�h�'], encoding='ISO-8859-1')
        self.failUnlessEqual(f.get(instance), ['h\xc3\xa9h\xc3\xa9h\xc3\xa9'])
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), ['h�h�h�'])
        f.set(instance, [u'h�h�h�'])
        self.failUnlessEqual(f.get(instance), ['h\xc3\xa9h\xc3\xa9h\xc3\xa9'])
        self.failUnlessEqual(f.get(instance, encoding="ISO-8859-1"), ['h�h�h�'])
            
class UnicodeTextFieldTest( unittest.TestCase ):
    
    def test_set(self):
        f = TextField('test')
        f.set(instance, 'h\xc3\xa9h\xc3\xa9h\xc3\xa9', mimetype='text/plain')
        self.failUnlessEqual(f.getRaw(instance), 'h\xc3\xa9h\xc3\xa9h\xc3\xa9')
        self.failUnlessEqual(f.getRaw(instance, encoding="ISO-8859-1"), 'h�h�h�')
        f.set(instance, 'h�h�h�', encoding='ISO-8859-1', mimetype='text/plain')
        self.failUnlessEqual(f.getRaw(instance), 'h\xc3\xa9h\xc3\xa9h\xc3\xa9')
        self.failUnlessEqual(f.getRaw(instance, encoding="ISO-8859-1"), 'h�h�h�')
        f.set(instance, u'h�h�h�', mimetype='text/plain')
        self.failUnlessEqual(f.getRaw(instance), 'h\xc3\xa9h\xc3\xa9h\xc3\xa9')
        self.failUnlessEqual(f.getRaw(instance, encoding="ISO-8859-1"), 'h�h�h�')
            
            
def test_suite():
    return unittest.TestSuite([unittest.makeSuite(UnicodeStringFieldTest),
                               unittest.makeSuite(UnicodeLinesFieldTest),
                               unittest.makeSuite(UnicodeTextFieldTest),
                               ])

if __name__=='__main__':
    unittest.main(defaultTest='test_suite')
