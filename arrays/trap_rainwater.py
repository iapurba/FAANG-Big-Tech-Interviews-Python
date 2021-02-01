#!/usr/bin/env python3

import unittest


def get_trapped_rainwater(heights:list):
    total_water = 0
    length = len(heights)

    for index, current_height in enumerate(heights):
        max_left = 0
        max_right = 0
        left_index = index
        right_index = index

        while left_index >= 0:
            max_left = max(max_left, heights[left_index])
            left_index -= 1

        while right_index < length:
            max_right = max(max_right, heights[right_index])
            right_index += 1

        current_water = min(max_left, max_right) - current_height

        if current_water > 0:
            total_water += current_water

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
