VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self, value):
        if value not in VALID_CARDS:
            raise Exception(f'{value} is not a valid card.')
        self.value = value
