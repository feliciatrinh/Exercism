# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/bob/canonical-data.json
# File last updated on 2023-07-20

import unittest

from bob import (
    response,
    response_regex
)


class BobTest(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(response("Tom-ay-to, tom-aaaah-to."), "Whatever.")
        self.assertEqual(response_regex("Tom-ay-to, tom-aaaah-to."), "Whatever.")

    def test_shouting(self):
        self.assertEqual(response("WATCH OUT!"), "Whoa, chill out!")
        self.assertEqual(response_regex("WATCH OUT!"), "Whoa, chill out!")

    def test_shouting_gibberish(self):
        self.assertEqual(response("FCECDFCAAB"), "Whoa, chill out!")
        self.assertEqual(response_regex("FCECDFCAAB"), "Whoa, chill out!")

    def test_asking_a_question(self):
        self.assertEqual(
            response("Does this cryogenic chamber make me look fat?"), "Sure."
        )
        self.assertEqual(
            response_regex("Does this cryogenic chamber make me look fat?"), "Sure."
        )

    def test_asking_a_numeric_question(self):
        self.assertEqual(response("You are, what, like 15?"), "Sure.")
        self.assertEqual(response_regex("You are, what, like 15?"), "Sure.")

    def test_asking_gibberish(self):
        self.assertEqual(response("fffbbcbeab?"), "Sure.")
        self.assertEqual(response_regex("fffbbcbeab?"), "Sure.")

    def test_talking_forcefully(self):
        self.assertEqual(response("Hi there!"), "Whatever.")
        self.assertEqual(response_regex("Hi there!"), "Whatever.")

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            response("It's OK if you don't want to go work for NASA."), "Whatever."
        )
        self.assertEqual(
            response_regex("It's OK if you don't want to go work for NASA."), "Whatever."
        )

    def test_forceful_question(self):
        self.assertEqual(
            response("WHAT'S GOING ON?"), "Calm down, I know what I'm doing!"
        )
        self.assertEqual(
            response_regex("WHAT'S GOING ON?"), "Calm down, I know what I'm doing!"
        )

    def test_shouting_numbers(self):
        self.assertEqual(response("1, 2, 3 GO!"), "Whoa, chill out!")
        self.assertEqual(response_regex("1, 2, 3 GO!"), "Whoa, chill out!")

    def test_no_letters(self):
        self.assertEqual(response("1, 2, 3"), "Whatever.")
        self.assertEqual(response_regex("1, 2, 3"), "Whatever.")

    def test_question_with_no_letters(self):
        self.assertEqual(response("4?"), "Sure.")
        self.assertEqual(response_regex("4?"), "Sure.")

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            "Whoa, chill out!",
        )
        self.assertEqual(
            response_regex("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            "Whoa, chill out!",
        )

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(response("I HATE THE DENTIST"), "Whoa, chill out!")
        self.assertEqual(response_regex("I HATE THE DENTIST"), "Whoa, chill out!")

    def test_statement_containing_question_mark(self):
        self.assertEqual(response("Ending with ? means a question."), "Whatever.")
        self.assertEqual(response_regex("Ending with ? means a question."), "Whatever.")

    def test_non_letters_with_question(self):
        self.assertEqual(response(":) ?"), "Sure.")
        self.assertEqual(response_regex(":) ?"), "Sure.")

    def test_prattling_on(self):
        self.assertEqual(response("Wait! Hang on. Are you going to be OK?"), "Sure.")
        self.assertEqual(response_regex("Wait! Hang on. Are you going to be OK?"), "Sure.")

    def test_silence(self):
        self.assertEqual(response(""), "Fine. Be that way!")
        self.assertEqual(response_regex(""), "Fine. Be that way!")

    def test_prolonged_silence(self):
        self.assertEqual(response("          "), "Fine. Be that way!")
        self.assertEqual(response_regex("          "), "Fine. Be that way!")

    def test_alternate_silence(self):
        self.assertEqual(response("\t\t\t\t\t\t\t\t\t\t"), "Fine. Be that way!")
        self.assertEqual(response_regex("\t\t\t\t\t\t\t\t\t\t"), "Fine. Be that way!")

    def test_multiple_line_question(self):
        self.assertEqual(
            response("\nDoes this cryogenic chamber make me look fat?\nNo."),
            "Whatever.",
        )
        self.assertEqual(
            response_regex("\nDoes this cryogenic chamber make me look fat?\nNo."),
            "Whatever.",
        )

    def test_starting_with_whitespace(self):
        self.assertEqual(response("         hmmmmmmm..."), "Whatever.")
        self.assertEqual(response_regex("         hmmmmmmm..."), "Whatever.")

    def test_ending_with_whitespace(self):
        self.assertEqual(
            response("Okay if like my  spacebar  quite a bit?   "), "Sure."
        )
        self.assertEqual(
            response_regex("Okay if like my  spacebar  quite a bit?   "), "Sure."
        )

    def test_other_whitespace(self):
        self.assertEqual(response("\n\r \t"), "Fine. Be that way!")
        self.assertEqual(response_regex("\n\r \t"), "Fine. Be that way!")

    def test_non_question_ending_with_whitespace(self):
        self.assertEqual(
            response("This is a statement ending with whitespace      "), "Whatever."
        )
        self.assertEqual(
            response_regex("This is a statement ending with whitespace      "), "Whatever."
        )
