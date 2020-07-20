# from random import seed #seems to work fine without seeding the rand int
# from random import randint

class Card:
    def __init__(self, number, suit):
        self._number = number
        #add underscore to attribute _suit to indicate that this property should not be accessed directly; designated getter and/or setter method should be used
        self._suit = suit
    def __repr__(self):
        return  '{} of {}'.format(str(self.number), self.suit)

    #getter method suit can be called to access property safely
    #@property is a 'decorator' wrapper required for getter method to say that its a property
    @property
    def suit(self):
        return self._suit

    #@self.setter is a required decorator for the setter method to say that its a property
    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "diamonds", "clubs", "spades"]:
            self._suit = suit
        else:
            print("Invalid suit")
    
    @property
    def number(self):
        return self._number
    
    @number.setter 
    def number(self, number):
        if number in range(2, 11):
            self._number = number
        elif number in ["j", "q", "k", "a"]:
            self._number = number
        else:
            print("Invalid number")





#instantiate Card with instance card (automatically generates card face value using a constructor method)
#card = Card(9, "hearts")
#print(card)
# card.number = 11 #returns "Invalid number" and card._number is unchanged
# print(card)