from random import seed #seems to work fine without seeding the rand int
from random import randint

# class Card:
#     def __init__(self, suit, number):
#         self.suit = suit
#         self.number = number

class Card:
    def __init__(self):
        self.suit = randint(1,4)
        self.value = randint(1,13)
        if self.suit == 1:
            self.suit = "hearts"
        elif self.suit == 2:
           self.suit = "clubs"
        elif self.suit == 3:
            self.suit = "spades"
        elif self.suit == 4:
            self.suit = "diamonds"
        if self.value == 1:
            self.value = "A"
        elif self.value == 11:
            self.value = "J"
        elif self.value == 12:
            self.value = "Q"
        elif self.value == 13:
            self.value = "K"
        self.card_string = 'this is a {} of {}'.format(self.value, self.suit)


#instantiate Card with instance card (automatically generates card face value using a constructor method)
card = Card()


print(card.card_string)

