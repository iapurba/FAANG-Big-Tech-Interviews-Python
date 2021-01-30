#!/usr/bin/env python3

import unittest


def get_container_with_most_water(heights:list):
    length = len(heights)
    max_area = 0
    for i in range(length):
        for j in range(i+1, length):
            height = min(heights[i], heights[j])
            width = j - i
            current_area = height * width
            if current_area > max_area:
                max_area = current_area
    return max_area


class TestContainerWithMostWater(unittest.TestCase):

    test_cases = [
        ([7,1,2,3,9], 28),
        ([], 0),
        ([5], 0),
        ([6,9,3,4,5,8], 32),
    ]

    def test_container_with_most_water(self):
        for heights, max_area in self.test_cases:
            self.assertEqual(get_container_with_most_water(heights), max_area)


if __name__ == '__main__':
    unittest.main()
