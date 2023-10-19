# This file is where we will run the game from.

from poker_components.cardDeck import CardDeck
from poker_components.player import npcPlayer as player
from poker_components.table import Table

def __main__():
    cardDeck = CardDeck()
    cardDeck.shuffle()
    game_table = Table("Table")
    for i in range(6):
        game_table.add_player(player(i)) 
        game_table.deal_player(i)
        print(game_table.players[i].hand)

if __name__ == "__main__":
    __main__()
