#!/usr/bin/env python3

import unittest


def build_string(string):
    build_array = []
    for item in string:
        if item != "#":
            build_array.append(item)
        else:
            if len(build_array):
                build_array.pop()
    return build_array


def backspace_compare(S:str, T:str):
    array_s = build_string(S)
    array_t = build_string(T)
    if array_s == array_t:
        return True
    return False


def backspace_compare_optimized(S:str, T:str):
    p1 = len(S) - 1
    p2 = len(T) - 1

    while p1 >= 0 or p2 >= 0:
        if S[p1] == "#" or T[p2] == "#":
            if S[p1] == "#":
                back_count = 2
                while back_count > 0:
                    p1 -= 1
                    back_count -= 1
                    if S[p1] == "#":
                        back_count += 2
            if T[p2] == "#":
                back_count = 2
                while back_count > 0:
                    p2 -= 1
                    back_count -= 1
                    if T[p2] == "#":
                        back_count += 2
        else:
            if S[p1] != T[p2]:
                return False
            else:
                p1 -= 1
                p2 -= 1
    return True


class TestBackspaceCompare(unittest.TestCase):
    test_cases = [
        ("ab#z", "ac#z", True),
        ("xy#z", "xx#y", False),
        # ("###", "#", True),
        ("", "", True),
        ("Pqr#s", "pqr#s", False),
        ("12###34", "12##33#4", True),
        ("same", "same", True),
    ]

    def test_backspace_compare(self):
        for string1, string2, expected in self.test_cases:
            self.assertEqual(backspace_compare(string1, string2), expected)
            self.assertEqual(
                backspace_compare_optimized(string1, string2), expected
            )


if __name__ == '__main__':
    unittest.main()
