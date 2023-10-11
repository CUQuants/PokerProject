import unittest

from card import Card
from suit import Suit
from hand_analysis.analyze_hand import analyzeHand

class TestAnalyzeHand(unittest.TestCase):
    def test_high_card(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(4, Suit.SPADES), Card(6, Suit.DIAMONDS), Card(8, Suit.CLUBS), Card(10, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 0.66, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(5, Suit.HEARTS), Card(7, Suit.DIAMONDS), Card(9, Suit.CLUBS), Card(11, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 0.7425, places=2)

        # Test 3
        cards = [Card(4, Suit.HEARTS), Card(6, Suit.DIAMONDS), Card(8, Suit.CLUBS), Card(10, Suit.SPADES), Card(12, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 0.825, places=2)

        # Test 4
        cards = [Card(5, Suit.CLUBS), Card(7, Suit.HEARTS), Card(9, Suit.SPADES), Card(11, Suit.DIAMONDS), Card(13, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 0.9075, places=2)

        # Test 5
        cards = [Card(6, Suit.DIAMONDS), Card(8, Suit.CLUBS), Card(10, Suit.HEARTS), Card(12, Suit.SPADES), Card(14, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 0.99, places=2)
    
    def test_one_pair(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(2, Suit.SPADES), Card(6, Suit.DIAMONDS), Card(8, Suit.CLUBS), Card(10, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 1.0, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(3, Suit.HEARTS), Card(7, Suit.DIAMONDS), Card(9, Suit.CLUBS), Card(11, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 1.0825, places=2)

        # Test 3
        cards = [Card(4, Suit.HEARTS), Card(4, Suit.CLUBS), Card(8, Suit.DIAMONDS), Card(10, Suit.SPADES), Card(12, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 1.165, places=2)

        # Test 4
        cards = [Card(6, Suit.CLUBS), Card(6, Suit.HEARTS), Card(9, Suit.SPADES), Card(11, Suit.DIAMONDS), Card(13, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 1.33, places=2)

        # Test 5
        cards = [Card(14, Suit.DIAMONDS), Card(14, Suit.SPADES), Card(10, Suit.HEARTS), Card(12, Suit.CLUBS), Card(13, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 1.99, places=2)

    def test_two_pair(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(2, Suit.SPADES), Card(6, Suit.DIAMONDS), Card(6, Suit.CLUBS), Card(10, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 2.165, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(3, Suit.HEARTS), Card(7, Suit.DIAMONDS), Card(7, Suit.CLUBS), Card(11, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 2.2475, places=2)

        # Test 3
        cards = [Card(4, Suit.HEARTS), Card(4, Suit.CLUBS), Card(8, Suit.DIAMONDS), Card(12, Suit.SPADES), Card(12, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 2.495, places=2)

        # Test 4
        cards = [Card(5, Suit.CLUBS), Card(5, Suit.HEARTS), Card(9, Suit.SPADES), Card(9, Suit.DIAMONDS), Card(13, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 2.4125, places=2)

        # Test 5
        cards = [Card(6, Suit.DIAMONDS), Card(6, Suit.SPADES), Card(14, Suit.CLUBS), Card(10, Suit.CLUBS), Card(14, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 2.66, places=2)

    def test_three_of_a_kind(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(2, Suit.SPADES), Card(2, Suit.DIAMONDS), Card(8, Suit.CLUBS), Card(10, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 3.0, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(3, Suit.HEARTS), Card(3, Suit.DIAMONDS), Card(9, Suit.CLUBS), Card(11, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 3.0825, places=2)

        # Test 3
        cards = [Card(4, Suit.HEARTS), Card(4, Suit.CLUBS), Card(4, Suit.DIAMONDS), Card(10, Suit.SPADES), Card(12, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 3.165, places=2)

        # Test 4
        cards = [Card(5, Suit.CLUBS), Card(5, Suit.HEARTS), Card(5, Suit.SPADES), Card(11, Suit.DIAMONDS), Card(13, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 3.2475, places=2)

        # Test 5
        cards = [Card(14, Suit.DIAMONDS), Card(14, Suit.SPADES), Card(6, Suit.HEARTS), Card(12, Suit.CLUBS), Card(14, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 3.99, places=2)

    def test_straight(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(3, Suit.SPADES), Card(4, Suit.DIAMONDS), Card(5, Suit.CLUBS), Card(6, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 4.11, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(4, Suit.HEARTS), Card(5, Suit.DIAMONDS), Card(6, Suit.CLUBS), Card(7, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 4.22, places=2)

        # Test 3 - Ace high straight(highest)
        cards = [Card(10, Suit.CLUBS), Card(11, Suit.SPADES), Card(12, Suit.HEARTS), Card(13, Suit.DIAMONDS), Card(14, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 4.99, places=2)

        # Test 4
        cards = [Card(10, Suit.CLUBS), Card(11, Suit.SPADES), Card(12, Suit.HEARTS), Card(13, Suit.DIAMONDS), Card(9, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 4.88, places=2)

        # Test 5 - Wheel straight(lowest)
        cards = [Card(2, Suit.HEARTS), Card(3, Suit.SPADES), Card(4, Suit.DIAMONDS), Card(5, Suit.CLUBS), Card(14, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 4.0, places=2)

    def test_flush(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(4, Suit.HEARTS), Card(6, Suit.HEARTS), Card(8, Suit.HEARTS), Card(10, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 5.66, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(5, Suit.SPADES), Card(7, Suit.SPADES), Card(9, Suit.SPADES), Card(11, Suit.SPADES)]
        self.assertAlmostEqual(analyzeHand(cards), 5.7425, places=2)

        # Test 3
        cards = [Card(4, Suit.DIAMONDS), Card(6, Suit.DIAMONDS), Card(8, Suit.DIAMONDS), Card(10, Suit.DIAMONDS), Card(12, Suit.DIAMONDS)]
        self.assertAlmostEqual(analyzeHand(cards), 5.825, places=2)

        # Test 4
        cards = [Card(5, Suit.CLUBS), Card(7, Suit.CLUBS), Card(9, Suit.CLUBS), Card(11, Suit.CLUBS), Card(13, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 5.9075, places=2)

        # Test 5
        cards = [Card(7, Suit.SPADES), Card(3, Suit.SPADES), Card(4, Suit.SPADES), Card(5, Suit.SPADES), Card(14, Suit.SPADES)]
        self.assertAlmostEqual(analyzeHand(cards), 5.99, places=2)

    def test_full_house(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(2, Suit.SPADES), Card(2, Suit.DIAMONDS), Card(8, Suit.CLUBS), Card(8, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 6.0, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(3, Suit.HEARTS), Card(3, Suit.DIAMONDS), Card(9, Suit.CLUBS), Card(9, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 6.0825, places=2)

        # Test 3
        cards = [Card(4, Suit.HEARTS), Card(4, Suit.CLUBS), Card(4, Suit.DIAMONDS), Card(10, Suit.SPADES), Card(10, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 6.165, places=2)

        # Test 4
        cards = [Card(5, Suit.CLUBS), Card(5, Suit.HEARTS), Card(5, Suit.SPADES), Card(11, Suit.DIAMONDS), Card(11, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 6.2475, places=2)

        # Test 5
        cards = [Card(6, Suit.DIAMONDS), Card(6, Suit.SPADES), Card(6, Suit.HEARTS), Card(12, Suit.CLUBS), Card(12, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 6.33, places=2)

    def test_four_of_a_kind(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(2, Suit.SPADES), Card(2, Suit.DIAMONDS), Card(2, Suit.CLUBS), Card(10, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 7.0, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(3, Suit.HEARTS), Card(3, Suit.DIAMONDS), Card(3, Suit.CLUBS), Card(11, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 7.0825, places=2)

        # Test 3
        cards = [Card(4, Suit.HEARTS), Card(4, Suit.CLUBS), Card(4, Suit.DIAMONDS), Card(4, Suit.SPADES), Card(12, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 7.165, places=2)

        # Test 4
        cards = [Card(12, Suit.CLUBS), Card(12, Suit.HEARTS), Card(12, Suit.SPADES), Card(12, Suit.DIAMONDS), Card(13, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 7.825, places=2)

        # Test 5
        cards = [Card(14, Suit.DIAMONDS), Card(14, Suit.SPADES), Card(14, Suit.HEARTS), Card(14, Suit.CLUBS), Card(6, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 7.99, places=2)

    def test_straight_flush(self):
        # Test 1
        cards = [Card(2, Suit.HEARTS), Card(3, Suit.HEARTS), Card(4, Suit.HEARTS), Card(5, Suit.HEARTS), Card(6, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 8.12375, places=2)

        # Test 2
        cards = [Card(3, Suit.SPADES), Card(4, Suit.SPADES), Card(5, Suit.SPADES), Card(6, Suit.SPADES), Card(7, Suit.SPADES)]
        self.assertAlmostEqual(analyzeHand(cards), 8.2475, places=2)

        # Test 3
        cards = [Card(10, Suit.CLUBS), Card(11, Suit.CLUBS), Card(12, Suit.CLUBS), Card(13, Suit.CLUBS), Card(9, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 8.99, places=2)

        # Test 4
        cards = [Card(10, Suit.CLUBS), Card(11, Suit.CLUBS), Card(12, Suit.CLUBS), Card(8, Suit.CLUBS), Card(9, Suit.CLUBS)]
        self.assertAlmostEqual(analyzeHand(cards), 8.86625, places=2)

        # Test 5
        cards = [Card(2, Suit.HEARTS), Card(3, Suit.HEARTS), Card(4, Suit.HEARTS), Card(5, Suit.HEARTS), Card(14, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 8.00, places=2)

    def test_royal_flush(self):
        cards = [Card(10, Suit.HEARTS), Card(11, Suit.HEARTS), Card(12, Suit.HEARTS), Card(13, Suit.HEARTS), Card(14, Suit.HEARTS)]
        self.assertAlmostEqual(analyzeHand(cards), 9.0, places=2)

if __name__ == '__main__':
    unittest.main()