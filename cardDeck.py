from card import Card
import random

class CardDeck:
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.cards)
