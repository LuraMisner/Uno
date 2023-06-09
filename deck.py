from card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.deck = []

        # Initialize the deck
        self.initialize_deck()

        # Shuffles the deck
        shuffle(self.deck)

    def initialize_deck(self):
        # Some cards appear twice in the deck
        for i in range(2):
            self.initialize_deck_helper('red')
            self.initialize_deck_helper('green')
            self.initialize_deck_helper('blue')
            self.initialize_deck_helper('yellow')

        # Wild cards appear 4 times each
        for i in range(4):
            self.deck.append(Card('wild', 'wild'))
            self.deck.append(Card('draw', 'wild'))

        # 0 Cards only appear once for each color
        self.deck.append(Card('0', 'red'))
        self.deck.append(Card('0', 'blue'))
        self.deck.append(Card('0', 'green'))
        self.deck.append(Card('0', 'yellow'))

    def initialize_deck_helper(self, color):
        # Adds cards 1-9, skip, reverse, and +2 for the color
        for i in range(1, 10):
            self.deck.append(Card(f'{i}', color))

        self.deck.append(Card('skip', color))
        self.deck.append(Card('rev', color))
        self.deck.append(Card('draw', color))

    def draw_card(self) -> Card:
        # If the deck is empty, shuffle it and refill it
        if len(self.deck) == 0:
            self.__init__()

        # Otherwise, pick the last card from the deck to remove
        drawing_card = self.deck.pop()
        return drawing_card
