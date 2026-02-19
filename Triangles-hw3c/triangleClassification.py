"""Module for classifying triangles based on side lengths."""


class TriangleClassification:
    """Classifies triangles based on three side lengths."""

    # Static method that returns what type of triangle is based on the 3 sides given
    @staticmethod
    def classify_triangle(side1: float, side2: float, side3: float):
        """Return the type of triangle given three side lengths."""
        triangle_type = ""

        # Checks to make sure each of the 3 sides are not the following errors
                # - Non-number Input
                # - Zero length
                # - Negative length
        for side in [side1, side2, side3]:
            if not isinstance(side, (float, int)):
                return "Non-number Input Error"
            if side == 0:
                return "Zero Edge Error"
            if side < 0:
                return "Negative Side Error"

        # Sorts the triangle to be from lowest side to greatest
        sides = sorted([side1, side2, side3])

        # Checks that the triangle is valid (a + b > c, where c is the greatest side)
        if sides[0] + sides[1] <= sides[2]:
            return "Invalid Triangle Error"

        # Classifies the triangle based on the side lengths' relationship
        # - Equilateral if all equal each other
        # - Isosceles if 2 sides equal each other
        # - Scalene if no sides equal each other
        if side1 == side2 and side2 == side3:
            triangle_type = "Equilateral"

            # Returns an equilateral triangle before right triangle check because it is not possible
            return f"{triangle_type} Triangle"
        if (
            (side1 == side2 and side1 != side3)
            or (side2 == side3 and side2 != side1)
            or (side1 == side3 and side1 != side2)
        ):
            triangle_type = "Isosceles"
        else:
            triangle_type = "Scalene"

        # Checks to see if the triangle is right by using the pythagorean theorem
            # - has a tolerance based on if floats are given
            # - returns the type with right triangle status
        if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9:
            return f"{triangle_type} Right Triangle"

        # Returns the type without right triangle status
        return f"{triangle_type} Triangle"