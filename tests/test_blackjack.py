import main
import pytest


def test_count_card_total():
    score = main.count_card_total([('Club', '2'), ('Heart', 'J')])
    assert score == 12


def test_manage_ace():
    assert False