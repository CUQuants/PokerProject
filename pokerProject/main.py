# This file is where we will run the game from.

from poker_components.cardDeck import CardDeck
from poker_components.player import npcPlayer as Player
# from poker_components.card import Card

def __main__():
    cardDeck = CardDeck()
    cardDeck.shuffle()
    players = []
    for i in range(6):
        player = Player(i)
        player.hand = cardDeck.deal()
        players.append(player)
        print(player.hand)



if __name__ == "__main__":
    __main__()
