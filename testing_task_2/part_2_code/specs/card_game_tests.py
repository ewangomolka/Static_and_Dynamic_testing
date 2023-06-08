import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 9)
        self.card2 = Card("Diamonds", 5)
        self.card3 = Card("Spades", 1)
        self.card4 = Card("Clubs", 3)
        self.cards = CardGame([self.card1, self.card2, self.card3, self.card4])

    def test_check_for_ace(self):
        expected = True
        actual = self.cards.check_for_ace(self.card3)
        self.assertEqual(expected, actual)

    def test_highest_card(self):
        expected = self.card1
        actual = self.cards.highest_card(self.card1, self.card2)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3, self.card4]
        expected = "You have a total of 18"
        actual = self.cards.cards_total(cards)
        self.assertEqual(expected, actual)