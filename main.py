from card import Card
from suit import Suit
from hand_analysis.analyze_hand import analyzeHand

print(Card(1, Suit(1)).suit.value)

cards = [Card(rank, Suit(1)) for rank in [6,7,2,1,5]]

print(cards)
#print(analyzeHand(cards))