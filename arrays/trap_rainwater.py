#!/usr/bin/env python3

import unittest


def get_trapped_rainwater(heights:list):
    total_water = 0
    left = 0
    right = len(heights) - 1
    max_left = 0
    max_right = 0

    while left < right:
        if heights[left] <= heights[right]:
            if heights[left] < max_left:
                total_water += max_left - heights[left]
            else:
                max_left = heights[left]
            left += 1
        else:
            if heights[right] < max_right:
                total_water += max_right - heights[right]
            else:
                max_right = heights[right]
            right -= 1

    return total_water


class TestTrapedRainwater(unittest.TestCase):
    test_cases = [
        ([0,1,0,2,1,0,3,1,0,1,2], 8),
        ([], 0),
        ([2,3,4], 0),
        ([5], 0),
        ([7,7,7], 0),
        ([5,0,0,0,0,1,2,3,4,3,2], 22),
        ([1,2,3,4,3,2,1], 0),
        ([1,6,1,1,1,9], 15),
    ]

    def test_get_traped_rainwater(self):
        for heights, total_water in self.test_cases:
            self.assertEqual(get_trapped_rainwater(heights), total_water)


if __name__ == '__main__':
    unittest.main()
