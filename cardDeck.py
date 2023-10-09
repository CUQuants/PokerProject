from card import Card
from suit import Suit
import random


class CardDeck:
    def __init__(self):
        self.ranks = range(2,14)
        self.suits = [e.value for e in Suit]
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return
