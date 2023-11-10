from pokerProject.poker_components.card import Card
from pokerProject.poker_components.suit import Suit

HIGH_CARD_POINTS= {11:6, 12:7, 13:8, 14:10}

def chenFormula(cards):
    
    if len(cards) != 2:
        #input validation
        return False
    
    power = 0
    #find highest of the two
    high_card = cards[1]
    if cards[0]>cards[1]:
        high_card = cards[0]

    #highest card
    if high_card.rank <= 10:
        power = high_card.rank/2.0
    else:
        power = HIGH_CARD_POINTS[high_card.rank]
    pair = False
    #pairs
    if cards[1].rank==cards[0].rank:
        pair = True
        power *=2
        if power<5:
            power = 5
        if cards[1].rank==5:
            power +=1
    
    #suited
    if cards[0].suit == cards[1].suit:
        power+=2
    
    #gappers
    gap = abs(cards[0].rank-cards[1].rank)
    if gap==1:
        power-=1
    elif gap==2:
        power-=2
    elif gap==3:
        power-=4
    elif gap>=4:
        power-=5

    if (gap==1 or gap==2) and high_card.rank<12 and not pair:
        power+=1
    
    return power