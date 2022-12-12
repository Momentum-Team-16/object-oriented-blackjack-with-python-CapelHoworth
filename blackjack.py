import random

SUITS = ['♥️', '♠️', '♦️', '♣️']
RANKS = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'({self.rank} {self.suit} ):'
        

class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def __str__(self):
        deck_as_string = ''
        for card in self.cards:
            deck_as_string += f'{card}  '
        return deck_as_string

    def shuffle(self):
        random.shuffle(self.cards)


class Game:
    def __init__(self):
            self.deck = Deck(SUITS, RANKS)
            self.deck.shuffle()
        # create a deck
        # shuffle a deck

new_game = Game()
print(new_game.deck)
