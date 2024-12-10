import random

class Deck:
    def __init__(self):
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        cards = [f'{value} of {suit}' for value in self.card_values.keys() for suit in self.suits]
        self.cards = cards
    
    def deal(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card