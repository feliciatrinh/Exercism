# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/collatz-conjecture/canonical-data.json
# File last updated on 2023-07-20

import unittest

from collatz_conjecture import (
    steps,
    steps_while
)


class CollatzConjectureTest(unittest.TestCase):
    def test_zero_steps_for_one(self):
        self.assertEqual(steps(1), 0)
        self.assertEqual(steps_while(1), 0)

    def test_divide_if_even(self):
        self.assertEqual(steps(16), 4)
        self.assertEqual(steps_while(16), 4)

    def test_even_and_odd_steps(self):
        self.assertEqual(steps(12), 9)
        self.assertEqual(steps_while(12), 9)

    def test_large_number_of_even_and_odd_steps(self):
        self.assertEqual(steps(1000000), 152)
        self.assertEqual(steps_while(1000000), 152)

    def test_zero_is_an_error(self):
        with self.assertRaises(ValueError) as err:
            steps(0)
        with self.assertRaises(ValueError) as err_while:
            steps_while(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(type(err_while.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Only positive integers are allowed")
        self.assertEqual(err_while.exception.args[0], "Only positive integers are allowed")

    def test_negative_value_is_an_error(self):
        with self.assertRaises(ValueError) as err:
            steps(-15)
        with self.assertRaises(ValueError) as err_while:
            steps_while(-15)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(type(err_while.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Only positive integers are allowed")
        self.assertEqual(err_while.exception.args[0], "Only positive integers are allowed")
