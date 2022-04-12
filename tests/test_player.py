from random import choices
from string import ascii_letters

from pytest import fixture, mark, param

from player import Player


@fixture
def player_instance(request) -> Player:
    p = Player(*request.param)
    return p


def get_name() -> str:
    name = "".join(choices(ascii_letters, k=6))
    return name


class TestPlayer:

    @mark.parametrize("player_instance, expected_res", (
            param((get_name(),), False, id="Human Player"),
            param((get_name(), True), True, id="Computer Player"),
    ), indirect=("player_instance",))
    def test_create(self, player_instance: Player, expected_res):
        assert player_instance.is_computer == expected_res
