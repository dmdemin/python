import unittest
from factorize_ import factorize


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ('string', 1.5)
        for t in cases:
            with self.subTest(x=t):
                self.assertRaises(TypeError, factorize, t)

    def test_negative(self):
        cases = (-1, -10, -100)
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(ValueError, factorize, case)

    def test_zero_and_one_cases(self):
        args = [0, 1]
        returns = [(0,), (1,)]

        for arg, ret in zip(args, returns):
            with self.subTest(x=arg):
                self.assertEqual(factorize(arg), ret)

    def test_simple_numbers(self):
        cases = (3, 13, 29)
        for case in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize(case), (case,))

    def test_two_simple_multipliers(self):
        cases = (6, 26, 121)
        returns = [(2, 3),
                   (2, 13),
                   (11, 11)]

        for arg, ret in zip(cases, returns):
            with self.subTest(x=arg):
                self.assertEqual(factorize(arg), ret)

    def test_many_multipliers(self):
        args = (1001, 9699690)
        returns = [(7, 11, 13),
                (2, 3, 5, 7, 11, 13, 17, 19)]

        for arg, ret in zip(args, returns):
            with self.subTest(x=arg):
                self.assertEqual(factorize(arg), ret)


if __name__ == '__main__':
    unittest.main()
