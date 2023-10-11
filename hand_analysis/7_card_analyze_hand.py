from card import Card
from suit import Suit
from hand_analysis.math_functions import linearInterpolation
'''
    0 - High Card(2 = 0.0, 14 = .99)
    1 - One Pair(2=1.0, 14(ace)=1.99)
    2 - Two Pair(2&3=2.0, 14+13=2.99)
    3 - Three of a Kind(2=3.0, 14=3.99)
    4 - Straight(2-6=4.0, 10-14=4.99)
    5 - Flush(2=5.0, 14=5.99)
    6 - Full House(2s&3s=6.0, 14s&13s=6.99)
    7 - Four of a Kind(2=7.0, 14=7.99)
    8 - Straight Flush(2-6=8.0, 9-13=8.99)
    9 - Royal Flush(always 9.0)
'''
STARTING_RANK = 2
NUM_RANKS = 13
NUM_SUITS = 4
CARDS_PER_DECK = 52

def analyzeHand(cards):
    """
    Takes in an array of 7 cards and returns the highest score in the hand
    """
    cards = sorted(cards)
    num_cards = len(cards)
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
    #TODO adapt this to work for hands that aren't 5 cards
    is_flush = False
    for i in range(NUM_SUITS):
        if suits[i]==num_cards:
            is_flush = True
            break
    #check for a straight
    is_straight = False
    num_in_row = 0
    prev = counts[-1]!=0
    #loop through counts looking for nonzero in an order of 5
    for i in range(NUM_RANKS):
        current = counts[i]!=0
        if current and prev:
            if num_in_row==0:
                num_in_row=2
            else:
                num_in_row+=1
        else:
            num_in_row = 0
        if num_in_row>=5:
            is_straight = True
        prev = current

    spread5 = cards[-1].rank-cards[0].rank
    spread4 = cards[-2].rank-cards[0].rank
    if is_flush:
        #flush
        score = linearInterpolation(cards[-1].rank, 5, 5.99)
        if spread5 ==4:
            if cards[0].rank==10:
                #royal flush
                score = 9
            else:
                #straight flush 
                score = linearInterpolation(cards[0].rank, 8, 8.99, minCard=1, maxCard=9)
        elif spread5 == 12 and spread4 == 3 and cards[0].rank == 2 and cards[-1].rank == 14:
            # TODO adapt for more than 5 cards
            #special case of 2345A
            score = linearInterpolation(1, 8, 8.99, minCard=1, maxCard=9)
    else:
        if is_straight:
            # TODO special case 2345A
            #straight
            score = linearInterpolation(cards[0].rank, 4, 4.99, minCard=1, maxCard=10)
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

    return score


def findRepeated(cards):
    """
    finds the first card value that is repeated the most in a given set of cards
    """
    max_reps = 0
    most_repeated_card = None
    card_counts = {}
    #O(n) complexity with a dictionary vs O(n^2) with nested loops
    
    for card in cards:
        value = card.rank
        if value in card_counts:
            card_counts[value] += 1
        else:
            card_counts[value] = 1

        if card_counts[value] > max_reps:
            max_reps = card_counts[value]
            most_repeated_card = value

    return most_repeated_card
    
def isStraight(cards):
    """
    checks a sorted array of 5 cards if they are in sequential order or not
    """
    cards_len = len(cards)
    for i in range(cards_len-1):
        if cards[i].rank+1!=cards[i+1].rank:
            return False
    return True

def isStraight7(cards):
    """
    checks a sorted array of 7 cards if they are in sequential order or not
    """
