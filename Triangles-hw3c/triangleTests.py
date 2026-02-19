import unittest
from triangleClassification import TriangleClassification as tc


# Class to perform the following tests of the triangle classification function
class test(unittest.TestCase):

    # Test to see if a triangle is Equilateral
    def test_equilateral(self):
        self.assertEqual(tc.classify_triangle(3, 3, 3), "Equilateral Triangle")

    # Test to see if a triangle is Isosceles
    def test_isosceles(self):
        self.assertEqual(tc.classify_triangle(3, 3, 4), "Isosceles Triangle")

    # Tests to see if a triangle is Scalene
    def test_scalene(self):
        self.assertEqual(tc.classify_triangle(3, 4, 6), "Scalene Triangle")

    # Tests to see if a triangle is right and Isosceles
    def test_right_isosceles(self):
        self.assertEqual(tc.classify_triangle(5, 7.07106781187, 5), "Isosceles Right Triangle")

    # Tests to see if a triangle is a right and Scalene
    def test_right_scalene(self):
        self.assertEqual(tc.classify_triangle(5, 3, 4), "Scalene Right Triangle")

    # Tests to see if a Non-number Input Error is given
    def test_nonNumber_input(self):
        self.assertEqual(tc.classify_triangle(1, 2, "hello"), "Non-number Input Error")

    # Tests to see if a Zero Edge Error is given for one side being zero
    def test_one_zero_input(self):
        self.assertEqual(tc.classify_triangle(1, 2, 0), "Zero Edge Error")

    # Tests to see if a Zero Edge Error is given for two sides being zero
    def test_two_zero_input(self):
        self.assertEqual(tc.classify_triangle(0, 2, 0), "Zero Edge Error")

    # Tests to see if a Zero Edge Error is given for all sides being zero
    def test_all_zero_input(self):
        self.assertEqual(tc.classify_triangle(0, 0, 0), "Zero Edge Error")

    # Tests to see if a Negative Side Error is given
    def test_negative_input(self):
        self.assertEqual(tc.classify_triangle(1, 2, -5), "Negative Side Error")

    # Tests to see if a Invalid Triangle Error is given
    def test_invalid_input(self):
        self.assertEqual(tc.classify_triangle(1, 2, 5), "Invalid Triangle Error")

# Runs all 11 tests
if __name__ == "__main__":
    unittest.main()
