#!/usr/bin/env python3

import unittest


def find_two_sum(nums:list, target:int):
    """
    Return indices of the two numbers that add up to a given target
    """
    nums_map = {}

    for index, current_map_val in enumerate(nums):
        if current_map_val in nums_map:
            return [nums_map[current_map_val], index]
        else:
            number_to_find = target - current_map_val
            nums_map[number_to_find] = index
    return None


class TestTwoSum(unittest.TestCase):

    test_cases = [
        ([1,3,7,9,2], 11, [3,4]),
        ([1,3,7,9,2], 25, None),
        ([], 1, None),
        ([5], 5, None),
        ([8,12], 20, [0,1])
    ]

    def test_find_two_sum(self):
        """Test find_two_sum function"""
        for nums, target, expected in self.test_cases:
            self.assertEqual(find_two_sum(nums, target), expected)


if __name__ == '__main__':
    unittest.main()
