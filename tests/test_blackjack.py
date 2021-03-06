import blackjack
import pytest


def test_count_card_total():
    score = blackjack.count_card_total([('Club', '2'), ('Heart', 'J')])
    assert score == 12
    score = blackjack.count_card_total([('Club', 'K'), ('Heart', 'J')])
    assert score == 20
    score = blackjack.count_card_total([('Club', 'K'), ('Heart', 'J'), ('Club', 'A')])
    assert score == 31


def test_manage_ace():
    test_hand_1 = [('Club', '2'), ('Club', 'A')]
    test_hand_2 = [('Club', 'A'), ('Heart', 'A')]
    test_hand_3 = [('Club', '2'), ('Diamond', '10'), ('Club', 'A')]

    assert blackjack.manage_ace(test_hand_1, 13) == 13
    assert blackjack.manage_ace(test_hand_2, 22) == 12
    assert blackjack.manage_ace(test_hand_3, 23) == 13


def test_hit_or_stay():
    deck = [('Club', '2'), ('Club', '10'), ('Club', 'A'), ('Club', '8')]

    deck, hand, points = blackjack.hit_or_stay(deck, [('Heart', '7'), ('Spade', '10')], 17)
    assert points == 17

    deck, hand, points = blackjack.hit_or_stay(deck, [('Heart', '7'), ('Spade', '5')], 12)
    assert points == 20

    deck, hand, points = blackjack.hit_or_stay(deck, [('Heart', '5'), ('Spade', '10')], 15)
    assert points == 26


def test_convert_cards_to_points():
    assert blackjack.convert_card_to_points(("Spade", "2")) == 2
    assert blackjack.convert_card_to_points(("Diamond", "K")) == 10
    assert blackjack.convert_card_to_points(("Club", "A")) == 11
