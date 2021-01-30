#!/usr/bin/env python3

import unittest


def get_container_with_most_water(heights:list):
    """
    Returns area of the container with most water
    """
    p1, p2 = 0, len(heights)-1
    max_area = 0

    while p1 < p2:
        height = min(heights[p1], heights[p2])
        width = p2 - p1
        current_area = height * width
        max_area = max(max_area, current_area)
        if heights[p1] <= heights[p2]:
            p1 += 1
        else:
            p2 -= 1
    return max_area


class TestContainerWithMostWater(unittest.TestCase):

    test_cases = [
        ([7,1,2,3,9], 28),
        ([], 0),
        ([5], 0),
        ([6,9,3,4,5,8], 32),
        ([4,8,1,2,3,9], 32),
        ([2,6,8,3,4,9,1], 24),
    ]

    def test_container_with_most_water(self):
        for heights, max_area in self.test_cases:
            self.assertEqual(get_container_with_most_water(heights), max_area)


if __name__ == '__main__':
    unittest.main()
