from unittest import mock

from pytest import mark, param, raises

from main import generate_players, get_players_count


class TestGame:
    @mark.parametrize("humans_count, computers_count, expected_count", (
            (1, 2, 3),
            (2, 0, 2),
            (0, 3, 3),
    ))
    def test_generate_players(self, humans_count, computers_count, expected_count):
        players_list = generate_players(humans_count, computers_count)
        assert len(players_list) == expected_count
        for player in players_list[:humans_count]:
            assert not player.is_computer
        for player in players_list[humans_count:]:
            assert player.is_computer

    @mark.parametrize("players_count", (
            param("5", id="Str of int"),
            param("smthng", id="Str of letters"),
            param(3, id="Int"),
            param(3.0, id="Float"),
    ))
    def test_get_players_count(self, players_count):
        with mock.patch('builtins.input', return_value=players_count):
            if not isinstance(players_count, (str, int, float)):
                with raises(ValueError):
                    get_players_count("")
            else:
                get_players_count("")
