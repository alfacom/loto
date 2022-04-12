from random import choice

from pytest import fixture

from card import Card


@fixture
def card_instance() -> Card:
    c = Card()
    return c


class TestCard:

    def test_card_elem(self, card_instance: Card):
        card = card_instance.card
        assert len(card) == 3
        for row in card:
            assert len(row) == 9

    def test_numbers(self, card_instance: Card):
        nums = card_instance.numbers
        assert len(nums) == card_instance.NUMBERS_COUNT
        assert len(nums) == len(set(nums))

    def test_crossout(self, card_instance: Card):
        crossout_num = choice(card_instance.numbers)
        assert card_instance.try_crossout_number(crossout_num)
        assert crossout_num not in card_instance.numbers
        assert not card_instance.try_crossout_number(crossout_num)
