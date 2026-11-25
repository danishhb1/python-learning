import random

# Card suits, ranks and their corresponding values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'
)

values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
    'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
    'Ten': 10, 'Jack': 11, 'Queen': 12,
    'King': 13, 'Ace': 14
}


# ==================== CARD CLASS ====================

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# ==================== DECK CLASS ====================

class Deck:

    def __init__(self):

        # Create an empty list to store all 52 cards
        self.all_cards = []

        # Create every possible combination of suit and rank
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):

        # Shuffle the deck randomly
        random.shuffle(self.all_cards)

    def deal_one(self):

        # Remove and return one card from the deck
        return self.all_cards.pop()


# ==================== PLAYER CLASS ====================

class Player:

    def __init__(self, name):
        self.name = name

        # Each player starts with an empty hand
        self.all_cards = []

    def remove_one(self):

        # Remove and return the first card
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        # Add multiple cards or a single card
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# ==================== GAME SETUP ====================

print('Welcome to the War Card Game!')

# Create two players
player_one = Player('One')
player_two = Player('Two')

# Create and shuffle a new deck
new_deck = Deck()
new_deck.shuffle()

# Deal 26 cards to each player
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(player_one)
print(player_two)

game_on = True
round_num = 0

# Prevent the game from running indefinitely
max_rounds = 10000


# ==================== GAME LOGIC ====================

while game_on:

    # Check whether Player One has run out of cards
    if len(player_one.all_cards) == 0:
        print('Player One is out of cards!')
        print('Player Two Wins!')
        game_on = False
        break

    # Check whether Player Two has run out of cards
    if len(player_two.all_cards) == 0:
        print('Player Two is out of cards!')
        print('Player One Wins!')
        game_on = False
        break

    # Stop the game if the maximum number of rounds is reached
    if round_num >= max_rounds:
        print('Maximum number of rounds reached!')
        print('The game ends in a draw.')
        game_on = False
        break

    round_num += 1
    print(f'\nRound {round_num}')

    # Reset the cards currently on the table
    player_one_cards = []
    player_two_cards = []

    # Each player places one card on the table
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        # Player One has the higher card
        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        # Player Two has the higher card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        # Both players have cards of equal value
        else:

            print('WAR!')

            # Check if both players have insufficient cards
            if len(player_one.all_cards) < 5 and len(player_two.all_cards) < 5:

                print('Neither player has enough cards for war!')
                print('The game ends in a draw.')

                game_on = False
                break

            # Check if Player One has enough cards
            elif len(player_one.all_cards) < 5:

                print('Player One is unable to play war!')
                print('Player Two Wins!')

                game_on = False
                break

            # Check if Player Two has enough cards
            elif len(player_two.all_cards) < 5:

                print('Player Two is unable to play war!')
                print('Player One Wins!')

                game_on = False
                break

            # Both players place five additional cards
            else:

                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


# ==================== GAME SUMMARY ====================

print('\nGame Over!')
print(f'Total rounds played: {round_num}')
