from poker_components.cardDeck import CardDeck
from poker_components.player import npcPlayer as Player

class Table:
    def __init__(self, name):
        self.pot = 0
        self.players = []
        self.current_bet = []
        self.deck = CardDeck()
        
    def add_player(self, player):
        self.players.append(player)
        
    def deal_player(self, player):
        self.players[player].recieve_card(self.deck.deal())
        return