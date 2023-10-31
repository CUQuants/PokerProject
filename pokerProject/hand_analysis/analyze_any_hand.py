from pokerProject.poker_components.card import Card
from pokerProject.poker_components.suit import Suit
from pokerProject.hand_analysis.simple_analysis import isStraight5, findRepeated
from pokerProject.hand_analysis.math_functions import linearInterpolation

#    Scoring for 2 cards:
#    chen formula
#    https://en.wikipedia.org/wiki/Texas_hold_%27em_starting_hands#Chen_formula 
#    Scoring for 5+ cards:
#    0 - High Card(2 = 0.0, 14 = .99)
#    1 - One Pair(2=1.0, 14(ace)=1.99)
#    2 - Two Pair(2&3=2.0, 14+13=2.99)
#    3 - Three of a Kind(2=3.0, 14=3.99)
#    4 - Straight(2-6=4.0, 10-14=4.99)
#    5 - Flush(2=5.0, 14=5.99)
#    6 - Full House(2s&3s=6.0, 14s&13s=6.99)
#    7 - Four of a Kind(2=7.0, 14=7.99)
#    8 - Straight Flush(2-6=8.0, 9-13=8.99)
#    9 - Royal Flush(always 9.0)

#Possible number of cards - 2,5,6,7

STARTING_RANK = 2
NUM_RANKS = 13
NUM_SUITS = 4
CARDS_PER_DECK = 52

def analyzeAnyHand(cards):
    """
    Takes in an array of cards and returns the score of the hand and the best hand out of the cards as a tuple
    """
    num_cards = len(cards)
    cards = sorted(cards)
    if num_cards ==2:
        #two cards
        #TODO  use the chen formula

        return
    elif(num_cards>5):
        #either 6 or 7 available cards
        #need to call this function recursively
        max_value = 0
        best_cards = []
        for i in range(0,num_cards):
            for j in range(i+1,num_cards):
                for k in range(j+1, num_cards):
                    for l in range(k+1,num_cards):
                        for m in range(l+1,num_cards):
                            score, temp_cards = analyzeAnyHand([cards[i],cards[j],cards[k],cards[l],cards[m]])
                            if score > max_value:
                                max_value = score
                                best_cards = temp_cards
        return (max_value,cards)
    elif num_cards==5:
        
        #5 cards to analyze
        #default to high card
        score = linearInterpolation(cards[-1].rank, 0, .99)
        counts = [0]*NUM_RANKS #number of each value in hand
        suits = [0]*NUM_SUITS # number of each rank in hand
        for i in range(num_cards):
            counts[cards[i].rank-STARTING_RANK]+=1
            suits[cards[i].suit.value]+=1
        
        #check for 2,3, and 4 of a kind
        pair_count = three_count = four_count = 0
        for i in range(NUM_RANKS):
            if counts[i]==2:
                pair_count+=1
            elif counts[i]==3:
                three_count+=1
            elif counts[i]==4:
                four_count+=1
        
        #check for a flush
        is_flush = False
        for i in range(NUM_SUITS):
            if suits[i]==num_cards:
                is_flush = True
                break
        #check for a straight
        spread5 = cards[-1].rank-cards[0].rank
        spread4 = cards[-2].rank-cards[0].rank

        if is_flush:
            #flush
            score = linearInterpolation(cards[-1].rank, 5, 5.99)
            if isStraight5(cards):
                if cards[0].rank==10:
                    #royal flush
                    score = 9
                else:
                    #straight flush 
                    score = linearInterpolation(cards[0].rank, 8, 8.99, minCard=1, maxCard=9)
            elif spread5 == 12 and spread4 == 3 and cards[0].rank == 2 and cards[-1].rank == 14:
                #special case of 2345A
                score = linearInterpolation(1, 8, 8.99, minCard=1, maxCard=9)
        else:
            if isStraight5(cards):
                #straight
                score = linearInterpolation(cards[0].rank, 4, 4.99, minCard=1, maxCard=10)
            elif spread5 == 12 and spread4 == 3 and cards[0].rank == 2 and cards[-1].rank == 14:
                #special case of 2345A
                score = linearInterpolation(1, 4, 4.99, minCard=1, maxCard=10)
            elif four_count == 1:
                #four of a kind
                score = linearInterpolation(findRepeated(cards), 7,7.99)
            elif three_count == 1:
                if pair_count ==1:
                    #full house
                    #is scored based on who has a higher 3 of a kind
                    score = linearInterpolation(findRepeated(cards), 6, 6.99)
                else:
                    #three of a kind
                    score = linearInterpolation(findRepeated(cards), 3,3.99)
            elif pair_count >=2:
                #two pair
                #NOTE this will only give a score based on the average of the two pairs, and may not always be accurate to the winner
                score_hi = linearInterpolation(findRepeated(cards[::-1]), 2.0, 2.99)
                score_lo = linearInterpolation(findRepeated(cards), 2.0, 2.99)
                score = (score_hi+score_lo)/2.0
            elif pair_count == 1:
                #one pair
                score = linearInterpolation(findRepeated(cards), 1.0,1.99)

        return (score,cards)
    else:
        #error
        return (-1,[])
