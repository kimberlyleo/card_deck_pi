from card import Card
import random

class Deck:
    def __init__(self):
        #the deck will store a list of cards, each will be a Card object
        self._cards = []
        self.populate()
        #print(self._cards)
    #method to populate the deck w the necessary 52 cards
    def populate(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"]
        cards = []
        for suit in suits:
            for number in numbers:
                cards.append( Card( number, suit))
            #could simplify using list comprehension: which produces of list  of Card objects using all possible iterations of suit and number
            #self._cards = [ Card(s, n) for s in suits for n in numbers ]
        self._cards = cards

    def shuffle():
my_deck = Deck()