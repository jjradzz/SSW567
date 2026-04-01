# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Scalene Right','3,4,5 is a Scalene Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene Right','5,3,4 is a Scalene Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsosceles(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isosceles', '3, 3, 4 should be isosceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3, 4, 6 should be scalene')

    def testRightIsosceles(self):
        self.assertEqual(classifyTriangle(5, 7.07106781187, 5), 'Isosceles Right', '5, 7.07106781187, 5 should be isosceles right')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(1, 2, 5), 'NotATriangle', '1, 2, 5 should be invalid')

    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(1, 2, -5), 'InvalidInput', '1, 2, -5 should be invalid')

    def testNonNumberInput(self):
        self.assertEqual(classifyTriangle(1, 2, "hello"), 'InvalidInput', '1, 2, hello should be invalid')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

