#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import math

class TestMathMethods(unittest.TestCase):

    def setUp(self):
        self.number = 3.5
        self.negativeNumber = -3.5

    def test_ceil(self):
        self.assertEqual(math.ceil(self.number), 4);
        self.assertEqual(math.ceil(self.negativeNumber), -3);

    def test_fabs(self):
        self.assertEqual(math.fabs(self.negativeNumber), 3.5);

    def test_floor(self):
        self.assertEqual(math.floor(self.number), 3);
        self.assertEqual(math.floor(self.negativeNumber), -4);

    def test_fmod(self):
        self.assertEqual(math.fmod(self.number,2), 1.5);
        self.assertEqual(math.fmod(self.negativeNumber, 2), -1.5);

    def test_fsum(self):
        self.assertEqual(math.fsum([2,4,3,6]), 15);

    def test_pow(self):
        self.assertEqual(math.pow(2,3), 8);

    def test_sqrt(self):
        self.assertEqual(math.sqrt(16), 4);

    def test_sqrt(self):
        self.assertEqual(math.sqrt(16), 4);

    def test_gamma(self):
        self.assertEqual(math.gamma(0.1), 9.513507698668732);

if __name__ == "__main__": 
    print ("running unittests for math")
    unittest.main();
