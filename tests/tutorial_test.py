#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   Takahiro Oshima <tarotora51@gmail.com>
# License:  MIT License
# Created:  2017-10-01
#
import unittest
from tutorial import countGridGraphSet

class TutorialTest(unittest.TestCase):
    def setup(self):
        print('setup Tutorial Test')

    def test_countGridGraphSet(self):
        self.assertEquals(countGridGraphSet(8), 3266598486981642)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TutorialTest))
    return suite
