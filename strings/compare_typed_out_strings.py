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


class TestBackspaceCompare(unittest.TestCase):
    test_cases = [
        ("ab#z", "ac#z", True),
        ("xy#z", "xx#y", False),
        ("###", "#", True),
        ("", "", True),
        ("Pqr#s", "pqr#s", False),
        ("12###34", "12##33#4", True),
        ("same", "same", True),
    ]

    def test_backspace_compare(self):
        for string1, string2, expected in self.test_cases:
            self.assertEqual(backspace_compare(string1, string2), expected)


if __name__ == '__main__':
    unittest.main()
