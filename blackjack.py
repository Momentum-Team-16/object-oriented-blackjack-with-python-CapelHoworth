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

    def deal_card(self, player):
        dealt_card = self.cards.pop()
        player.player_hand.append(dealt_card)


class Dealer:
    def __init__(self):
        self.player_hand = []
        self.name = 'dealer'

    def __str__(self):
        return self.name

    def show_hand(self):
        hand_as_string = ''
        for card in self.player_hand:
            hand_as_string += f'{card}'
        return hand_as_string

    def hide_hand(self):
        self.player_hand[1] = ' (__)'
        hand_as_string = ''
        for card in self.player_hand:
            hand_as_string += f'{card}'
        return hand_as_string


class Player:
    def __init__(self):
        self.player_hand = []
        self.name = 'player'
    
    def __str__(self):
        return self.name

    def show_hand(self):
        hand_as_string = ''
        for card in self.player_hand:
            hand_as_string += f'{card}'
        return hand_as_string


# class User:
#     def __init__(self):
#         self.player_hand = []


class Game:
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)
        self.deck.shuffle()
        self.players = []
        self.dealer = Dealer()

    def deal_players(self):
        while len(self.dealer.player_hand) < 2:
            for player in self.players:
                self.deck.deal_card(player)

    def create_players(self):
        number = input('How many players, player?')
        number = int(number)
        counter = 1
        while len(self.players) < number:
            player = Player()
            player.name = f'Player {counter}'
            self.players.append(player)
            counter += 1
        self.players.append(self.dealer)


new_game = Game()
new_game.create_players()
new_game.deal_players()

for person in new_game.players:
    if person != new_game.dealer:
        print(person, person.show_hand())
    else:
        print(person, person.hide_hand())

# print(f'Player1 hand: {new_game.player1}')
# print(f'Player2 hand: {new_game.player2}')
# print(f'Dealer hand: {new_game.dealer}')
