import unittest

from pokerProject.poker_components.card import Card
from pokerProject.poker_components.suit import Suit
from pokerProject.hand_analysis.chen_formula import chenFormula

class TestChenFormula(unittest.TestCase):
    def test_high_card(self):
        # Test 1
        cards = [Card(14, Suit.HEARTS), Card(2, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 5)
        # Test 2
        cards = [Card(13, Suit.HEARTS), Card(2, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 3)

        # Test 3
        cards = [Card(11, Suit.HEARTS), Card(2, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 1)

        # Test 4
        cards = [Card(10, Suit.HEARTS), Card(2, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 0)

        # Test 5
        cards = [Card(8, Suit.HEARTS), Card(2, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), -1)

        # Test 6
        cards = [Card(6, Suit.HEARTS), Card(2, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), -2)

    def test_pair(self):
        # Test 1
        cards = [Card(14, Suit.HEARTS), Card(14, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 20)

        # Test 2
        cards = [Card(13, Suit.HEARTS), Card(13, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 16)

        # Test 3
        cards = [Card(2, Suit.HEARTS), Card(2, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 5)

        # Test 4
        cards = [Card(10, Suit.HEARTS), Card(10, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 10)
    
    def test_suited_gaps(self):
        # 10 8 suited -> 7
        cards = [Card(10, Suit.HEARTS), Card(8, Suit.HEARTS)]
        self.assertEqual(chenFormula(cards), 7)

        # 6 4 suited -> 5
        cards = [Card(6, Suit.HEARTS), Card(4, Suit.HEARTS)]
        self.assertEqual(chenFormula(cards), 5)

        # A K suited -> 12
        cards = [Card(14, Suit.HEARTS), Card(13, Suit.HEARTS)]
        self.assertEqual(chenFormula(cards), 12)

        # 7 J suited -> 4
        cards = [Card(7, Suit.HEARTS), Card(11, Suit.HEARTS)]
        self.assertEqual(chenFormula(cards), 4)

        # A 2 suited -> 5
        cards = [Card(14, Suit.HEARTS), Card(2, Suit.HEARTS)]
        self.assertEqual(chenFormula(cards), 3)
    
    def test_gaps(self):
    # Test 1
        cards = [Card(10, Suit.HEARTS), Card(8, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 5)

        # Test 2
        cards = [Card(14, Suit.HEARTS), Card(2, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 5)

        # Test 3
        cards = [Card(6, Suit.HEARTS), Card(4, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 3)

        # Test 4
        cards = [Card(2, Suit.HEARTS), Card(7, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), -1)

        # Test 5
        cards = [Card(10, Suit.HEARTS), Card(7, Suit.SPADES)]
        self.assertEqual(chenFormula(cards), 3)
    
    
