#
# Skeleton Archetypes test
#

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from common import *
from utils import *

class TestSomething(ArchetypesTestCase):

    def afterSetUp(self):
        ArchetypesTestCase.afterSetUp(self)
        # more

    def beforeTearDown(self):
        # more
        ArchetypesTestCase.beforeTearDown(self)

    def testSomething(self):
        # Test something
        self.failUnless(1==1)


if __name__ == '__main__':
    framework()
else:
    # While framework.py provides its own test_suite()
    # method the testrunner utility does not.
    import unittest
    def test_suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestSomething))
        return suite
