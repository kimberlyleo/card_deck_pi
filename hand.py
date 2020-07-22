class Hand:
    def __init__(self):
        self._hand = []
        # self.deal_hand()

    def deal_hand(self, cards_per_hand, cards):
        hand = []
        for _ in range(cards_per_hand):
            hand.append(cards.pop())
        self._hand = hand

    @property
    def hand(self):
        return self._hand
    
    @hand.setter
    def hand(self,new_cards):
        self._hand.append(new_cards)