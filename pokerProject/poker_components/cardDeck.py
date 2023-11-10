from poker_components.card import Card
from poker_components.suit import Suit
import random

class CardDeck:
    def __init__(self):
        self.ranks = range(2,14)
        self.suits = [e.value for e in Suit]
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        #TODO implement deal function
        return self.cards.pop()
        
        
        return
