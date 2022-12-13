import random
import os

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
            deck_as_string += f'{card} '
        return deck_as_string

    def shuffle(self):
        random.shuffle(self.cards)


class Game:
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)
        self.deck.shuffle()

    def deal_card(self, player):
        dealt_card = self.deck.cards.pop()
        player.player_hand.append(dealt_card)


class Dealer:
    def __init__(self):
        self.player_hand = []

    def __str__(self):
        hand_as_string = ''
        for card in self.player_hand:
            hand_as_string += f'{card}'
        return hand_as_string


class Player:
    def __init__(self):
        self.player_hand = []
    
    def __str__(self):
        hand_as_string = ''
        for card in self.player_hand:
            hand_as_string += f'{card}'
        return hand_as_string


player1 = Player()
dealer = Dealer()
new_game = Game()


while len(player1.player_hand and dealer.player_hand) < 2:
    new_game.deal_card(player1)
    new_game.deal_card(dealer)


print(f'Player1 hand: {player1}')
print(f'Dealer hand: {dealer}')
print(new_game.deck)