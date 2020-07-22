from card import Card
from hand import Hand
import random

class Deck:
    def __init__(self):
        #the deck will store a list of cards, each will be a Card object
        self._cards = []
        self.populate()
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

    def shuffle(self):
        random.shuffle(self._cards)
        # print(self._cards)
    
    @property
    def cards(self):
        return self._cards
    
    def play_card(self, number, suit):
        pass
    
    def play_game():
        pass
        #provide number of players and cards_per_hand arguments here  
        # call deal for each round

    def deal(self, players):
        all_player_cards = {}
        for i in range(players):
            hand = []
            hand.append(Hand()) 
            all_player_cards[(i + 1)] = hand
            
            # for _ in range(cards_per_hand):
            #     player_hand.append(self._cards.pop())
            
        return all_player_cards
        # random set of cards and remove all
        # or just allow pull random to take number of cards as argument
    




my_deck = Deck()

#call shuffle() property of Deck on my_deck and the list is mutated 
#my_deck.shuffle()

#calling getter method to return shuffled deck
# print(my_deck.cards)

#dealing a round for a game with 3 players with 4 cards per hand
print(my_deck.deal(3,4))