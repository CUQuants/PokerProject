from pokerProject.poker_components import cardDeck
from pokerProject.hand_analysis import analyze_any_hand

# to be called when there are 4 cards on the table
def findOuts(hand, public_cards):
    hand = hand + public_cards
    baseline = analyze_any_hand(hand)#gets the baseline score of what we already have
    outs = 0
    # first remove hand and table cards from the deck
    deck = CardDeck()
    for card in hand:
        deck.cards.remove(card)
    #now we loop through all of the cards to see what would improve our hand
    for card in deck.cards:
        hand.append(card)
        if analyze_any_hand(hand) > baseline:
            outs += 1
        hand.remove(card)

    return outs