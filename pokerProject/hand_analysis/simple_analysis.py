from pokerProject.poker_components.card import Card
from pokerProject.poker_components.suit import Suit

def isStraight5(cards):
    """
    checks a sorted array of 5 cards if they are in sequential order or not
    """
    cards_len = len(cards)
    for i in range(cards_len-1):
        if cards[i].rank+1!=cards[i+1].rank:
            return False
    return True

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
    
