# This file is where we will run the game from.

from poker_components.cardDeck import CardDeck
from poker_components.player import Player
from poker_components.table import Table

def __main__():
    cardDeck = CardDeck()
    cardDeck.shuffle()
    game_table = Table("Table")
    for i in range(6):
        game_table.add_player(Player(i))
        game_table.deal_player(i)
        game_table.deal_player(i)
        game_table.active_players += 1
        print(game_table.players[i].hand)
        game_table.pot += game_table.current_bet;
        game_table.players[i].balance -= game_table.current_bet;
            
    while game_table.active_players > 1:
        for i in range(len(game_table.players)):
            # game_table.current_turn = i
            game_table.play(i)
            
    

if __name__ == "__main__":
    __main__()
