from random import sample, shuffle
from typing import List

from prettytable import PrettyTable, NONE


class Card:
    def __init__(self, card_name: str = ''):
        self.numbers = sample(range(1, 91), 15)
        self.card_name = card_name
        self.card = self.set_card()

    def __repr__(self) -> PrettyTable:
        table_card = PrettyTable(header=False, vrules=NONE, title=self.card_name)
        table_card.add_rows(self.card)
        return table_card.get_string()

    def set_card(self) -> List[List[int]]:
        table_numbers = []
        for i in range(3):
            nums = self.numbers[i * 5:i * 5 + 5]
            nums.extend(['' for _ in range(4)])
            shuffle(nums)
            table_numbers.append(nums)
        return table_numbers

    def try_crossout_number(self, number: int) -> bool:
        for i in self.card:
            if number not in i:
                continue
            index = i.index(number)
            i[index] = '-'
            self.numbers.remove(number)
            return True
        return False
