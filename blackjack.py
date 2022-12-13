import random
import os
import time

SUITS = ['♥️', '♠️', '♦️', '♣️']
RANKS = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
FACE = ['K', 'Q', 'J']


def play_again():
    replay = input("\n Deal another? y / n").lower()
    while replay not in ["yes", "no", "y", "n"]:
        print("\n Not valid input.")
        replay = input("\n Deal another? y / n").lower()

    if replay in ["y", "yes"]:
        play_again()
    else:
        print("\n Have fun out there in the human world!")
        os.system('clear')


def sleep_clear(num):
    time.sleep(num)
    os.system('clear')


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


class Player:
    def __init__(self):
        self.player_hand = []
        self.name = 'player'
        self.score = 0
    
    def __str__(self):
        return self.name

    def show_hand(self):
        hand_as_string = ''
        for card in self.player_hand:
            hand_as_string += f'{card}'
        return hand_as_string

    def deal_card(self, game):
        dealt_card = game.deck.cards.pop()
        self.player_hand.append(dealt_card)
        game.calculate_score(self)


class Dealer(Player):
    def hide_hand(self):
        self.player_hand[1] = ' (__)'
        hand_as_string = ''
        for card in self.player_hand:
            hand_as_string += f'{card}'
        return hand_as_string


class Game:
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)
        self.deck.shuffle()
        self.players = []
        self.dealer = Dealer()

    def deal_players(self):
        while len(self.dealer.player_hand) < 2:
            for player in self.players:
                player.deal_card(self)

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

    def calculate_score(self, player):
        player.score = 0
        num_ace = 0
        for card in player.player_hand:
            if card.rank in range(2, 11):
                player.score += card.rank
            elif card.rank in FACE:
                player.score += 10
            else:
                player.score += 11
                num_ace += 1
            while num_ace and player.score > 21:
                player.score -= 10
                num_ace -= 1


def play_game():
    print('♣️♦️ BLACKJACK ♠️♥️')
    new_game = Game()
    new_game.create_players()
    new_game.deal_players()

    for person in new_game.players:
        if person != new_game.dealer:
            print(person, person.show_hand())
            #print(person.score)
        else:
            print(person, person.hide_hand())
            #print(person.score)


if __name__ == "__main__":
    play_game()