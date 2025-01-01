# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/reverse-string/canonical-data.json
# File last updated on 2024-02-28

import unittest

from reverse_string import (
    reverse,
    reverse_list
)


class ReverseStringTest(unittest.TestCase):
    def test_an_empty_string(self):
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse_list(""), "")

    def test_a_word(self):
        self.assertEqual(reverse("robot"), "tobor")
        self.assertEqual(reverse_list("robot"), "tobor")

    def test_a_capitalized_word(self):
        self.assertEqual(reverse("Ramen"), "nemaR")
        self.assertEqual(reverse_list("Ramen"), "nemaR")

    def test_a_sentence_with_punctuation(self):
        self.assertEqual(reverse("I'm hungry!"), "!yrgnuh m'I")
        self.assertEqual(reverse_list("I'm hungry!"), "!yrgnuh m'I")

    def test_a_palindrome(self):
        self.assertEqual(reverse("racecar"), "racecar")
        self.assertEqual(reverse_list("racecar"), "racecar")

    def test_an_even_sized_word(self):
        self.assertEqual(reverse("drawer"), "reward")
        self.assertEqual(reverse_list("drawer"), "reward")

    def test_wide_characters(self):
        self.assertEqual(reverse("子猫"), "猫子")
        self.assertEqual(reverse_list("子猫"), "猫子")
