"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

ACE_CARD = 'A'

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in ['J', 'Q', 'K']:
        scoring_value = 10
    elif card == ACE_CARD:
        scoring_value = 1
    else:
        scoring_value = int(card)
    return scoring_value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one > value_card_two:
        higher_value_card = card_one
    elif value_card_two > value_card_one:
        higher_value_card = card_two
    else:
        higher_value_card = card_one, card_two
    return higher_value_card


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if ACE_CARD in (card_one, card_two):
        ace_value = 1
    elif value_of_card(card_one) + value_of_card(card_two) >= 11:
        ace_value = 1
    else:
        ace_value = 11
    return ace_value

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one == ACE_CARD:
        total = 11 + value_of_card(card_two)
    elif card_two == ACE_CARD:
        total = 11 + value_of_card(card_one)
    else:
        total = value_of_card(card_one) + value_of_card(card_two)
    return total == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
