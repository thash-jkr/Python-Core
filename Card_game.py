import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_cards(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_count = 0

while game_on:
    round_count += 1
    print(f'Round number {round_count}')

    if len(player_one.all_cards) == 0:
        print("Player One's card ran out! Player Two has won")
        game_on = False
    if len(player_two.all_cards) == 0:
        print("Player Two's card ran out! Player One has won")
        game_on = False

    # New Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_cards())

    player_two_cards = []
    player_two_cards.append(player_two.remove_cards())

    at_war = True

    while at_war:
        if player_one_cards[-1].values > player_two_cards[-1].values:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_two_cards[-1].values > player_one_cards[-1].values:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!!!')

            if len(player_one.all_cards) < 7:
                print('Player one is out of cards')
                print('Player Two WON!!!')
                game_on = False
                break

            elif len(player_two.all_cards) < 7:
                print('Player two is out of cards')
                print('Player One WON!!!')
                game_on = False
                break

            else:
                for num in range(7):
                    player_one_cards.append(player_one.remove_cards())
                    player_two_cards.append(player_two.remove_cards())
