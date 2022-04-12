from random import shuffle
from typing import List, Optional

from player import Player


def get_players_count(txt: str) -> Optional[int]:
    try:
        players_count = int(input(f"Введите кол-во участвующих {txt}: "))
    except ValueError:
        return None
    return players_count


def generate_players(player_count, computers_count) -> List[Player]:
    players_list = [Player(f'Player {i}') for i in range(player_count)]
    computers_list = [Player(f'Computer {i}', is_computer=True) for i in range(computers_count)]
    return players_list + computers_list


def game_on(players: List[Player]) -> None:
    numbers = [i for i in range(1, 91)]
    shuffle(numbers)
    winner = False
    while not winner:
        new_number = numbers.pop()
        print(f'Новый бочонок: {new_number} (осталось {len(numbers)})')
        for player in players.copy():
            print(player.card)
            answear = ''
            if player.is_computer and new_number in player.card.numbers:
                answear = 'y'
            if not player.is_computer:
                answear = input(f'{player.name}, зачеркнуть цифру {new_number}? (y/n)')
            if answear == 'y':
                if not player.crossout_number(new_number):
                    print(f'{player.name} пытался зачеркнуть цифру {new_number}, '
                          f'которой нет на его карте и проигрывает')
                    players.remove(player)
                else:
                    print(f'{player.name} зачеркнул цифру {new_number} на своей карте и продолжает игру')
            else:
                if new_number in player.card.numbers:
                    print(f'{player.name} не пытался зачеркнуть цифру {new_number}, '
                          f'которая есть на его карте и проигрывает')
                    players.remove(player)
                else:
                    print(f'{player.name} не нашел цифру {new_number} на своей карте и продолжает игру')
            if len(player.card.numbers) == 0:
                winner = True
                print(f'{player.name} первым вычеркивает все цифры на своей карте и выигрывает!')
                break


def main() -> None:
    players_count = get_players_count('людей')
    computers_count = get_players_count('компьютеров')
    if players_count is None or computers_count is None:
        print('Ответ должен быть цифрой')
        return
    players = generate_players(players_count, computers_count)
    game_on(players)
    print('Игра закончилась, спасибо всем за участие!')


if __name__ == '__main__':
    main()
