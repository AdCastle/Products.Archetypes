"""
"""
__author__ = 'Christian Heimes'
__docformat__ = 'restructuredtext'

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Testing import ZopeTestCase

# a list of dotted paths to modules which contains doc tests
DOCTEST_MODULES = (
    'Products.Archetypes.registry.base',
    )

from Products.Archetypes.tests.attestcase import ATTestCase
from Products.Archetypes.tests.doctestcase import ZopeDocTestSuite

def test_suite():
    suite = ZopeDocTestSuite(test_class=ATTestCase,
                             extraglobs={},
                             *DOCTEST_MODULES
                             )
    return suite

if __name__ == '__main__':
    framework()
