import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))


from Testing import ZopeTestCase

from Products.Archetypes.tests.attestcase import ATTestCase
from Products.Archetypes.atapi import *
from Products.Archetypes.config import PKG_NAME
from Products.Archetypes.schema import Schemata
from Products.Archetypes.schema import getNames

from DateTime import DateTime
import unittest

schema = BaseSchema

class Dummy(BaseContent):
    schema = schema


class SchemataTest( ATTestCase ):

    def afterSetUp(self):
        registerType(Dummy)
        content_types, constructors, ftis = process_types(listTypes(), PKG_NAME)
        self._dummy = Dummy(oid='dummy')

    def test_availschemata(self):
        dummy = self._dummy
        schemata = dummy.Schemata()
        keys = schemata.keys()
        keys.sort()
        self.assertEqual(keys, ['default', 'metadata'])

    def test_nameschemata(self):
        dummy = self._dummy
        schemata = dummy.Schemata()
        self.assertEqual(schemata['default'].getName(), 'default')
        self.assertEqual(schemata['metadata'].getName(), 'metadata')

    def test_baseschemata(self):
        dummy = self._dummy
        schemata = dummy.Schemata()
        base_names = getNames(schemata['default'])
        self.assertEqual(base_names, ['id', 'title'])

    def test_metaschemata(self):
        dummy = self._dummy
        schemata = dummy.Schemata()
        meta_names = getNames(schemata['metadata'])
        self.assertEqual(meta_names, ['allowDiscussion', 'subject',
                                      'description', 'contributors',
                                      'creators', 'effectiveDate',
                                      'expirationDate', 'language',
                                      'rights', 'creation_date',
                                      'modification_date'])


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(SchemataTest))
    return suite

if __name__ == '__main__':
    framework()
