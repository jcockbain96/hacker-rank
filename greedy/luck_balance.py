import sys
import unittest


def luck_balance(k, contests):
    arr.sort()
    least = min(abs(x - y) for x, y in zip(arr, arr[1:]))
    return least


class Tests(unittest.TestCase):
    def test1(self):
        data = [3, - 7, 0]
        self.assertEqual(min_abs_diff(data), 3)

    def test2(self):
        data = [1, -3, 71, 68, 17]
        self.assertEqual(min_abs_diff(data), 3)


if __name__ == "__main__":
    unittest.main()
