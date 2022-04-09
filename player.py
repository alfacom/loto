from card import Card


class Player:
    def __init__(self, name: str, is_computer: bool = False):
        self.name = name
        self.is_computer = is_computer
        self.card = Card(card_name=name)

    def crossout_number(self, number: int) -> bool:
        return self.card.try_crossout_number(number)
