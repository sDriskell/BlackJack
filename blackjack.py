"""
Shane Driskell
Blackjack Simulator
Runs multiple hands of Blackjack to simulate chances to win with starting
hand versus the dealer.
"""
import random
from pandas import *

RESULTS_TABLE = [[0 for x in range(1, 12)] for y in range(1, 12)]


def create_deck():
    """Create a deck of cards"""
    card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suit = ["Club", "Diamond", "Heart", "Spade"]
    deck = []

    for type in suit:
        for value in card:
            deck.append((type, value))
    random.shuffle(deck)
    return deck


def deal_hand(deck: list):
    """Deal cards for player/dealer's hand"""
    hand = []
    for deal in range(1, 3):
        hand.append(deck.pop())
    return hand


def count_card_total(hand: list):
    """Tally points in hand"""
    points = 0
    for item in hand:
        if item[1] in ['J', 'Q', 'K']:
            points += 10
        elif item[1] == 'A':
            points += 11
        else:
            points += int(item[1])
    return points


def manage_ace(hand: list, points):
    """Determine 1 or 11 points for Ace"""
    for card in hand:
        if card[1] == 'A' and points > 21:
            points -= 10
    return points


def compare_hands(player_points, dealer_points):
    """Winningness of initially dealt hand"""
    if player_points == 22:
        return 0, 1
    elif player_points <= dealer_points:
        return 0, 1
    else:
        return 1, 0


def hit_or_stay(deck: list, hand: list, points):
    """Determine to hit if less than 16 points in hand"""
    while points <= 16:
        hand.append(deck.pop())
        points = count_card_total(hand)
    return deck, hand, points


def convert_card_to_points(card):
    """Convert the card to a point value instead of face"""
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)
    # I feel this would be better if I took a hand: list and returned a tuple of ints.


def track_chance_to_win(player_hand: list, dealer_hand: list):
    """Generate number of wins per hand combination"""
    dealer_points = count_card_total(dealer_hand)
    dealer_points = manage_ace(dealer_hand, dealer_points)

    player_card_0 = convert_card_to_points(player_hand[0][1])
    player_card_1 = convert_card_to_points(player_hand[1][1])

    player_points = player_card_0 + player_card_1

    if player_points > dealer_points and player_points < 22:
        RESULTS_TABLE[player_card_0 - 1][player_card_1 - 1] += 1


def chance_to_win_percentage(games):
    """Turn table into a percentage chart"""
    for i in range(1, len(RESULTS_TABLE)):
        for j in range(1, len(RESULTS_TABLE)):
            card_win_percentage = RESULTS_TABLE[i][j]
            card_win_percentage = (card_win_percentage/games)*100
            RESULTS_TABLE[i][j] = f"{card_win_percentage:.2f}"


def visualize_chance_to_win():
    """Generate visual table of card chances"""
    print(DataFrame(RESULTS_TABLE,
          columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
          index=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]))


#TODO: Make manual Blackjack game
def manual_blacK_jack():
    pass


def automatic_black_jack():
    """Automatically run the game(s) and generate statistical data from it"""
    win_total = 0
    loss_total = 0

    chance_win_total = 0
    chance_loss_total = 0
    games_played_counter = 0

    games = int(input("How many games do you want to simulate? "))

    while games_played_counter < games:
        games_played_counter += 1
        deck = create_deck()

        player_hand = deal_hand(deck)
        dealer_hand = deal_hand(deck)

        player_points = count_card_total(player_hand)
        dealer_points = count_card_total(dealer_hand)

        player_points = manage_ace(player_hand, player_points)
        dealer_points = manage_ace(dealer_hand, dealer_points)

        win, loss = compare_hands(player_points, dealer_points)
        chance_win_total += win
        chance_loss_total += loss

        track_chance_to_win(player_hand, dealer_hand)

        deck, player_hand, player_points = hit_or_stay(deck,
                                                       player_hand,
                                                       player_points)
        deck, dealer_hand, dealer_points = hit_or_stay(deck,
                                                       dealer_hand,
                                                       dealer_points)

        win, loss = compare_hands(player_points,dealer_points)
        win_total += win
        loss_total += loss

        player_hand.clear()
        dealer_hand.clear()

    print("Chance to win: ", chance_win_total)
    print("Chance to lose: ", chance_loss_total)
    print("-"*20)
    print("Win: ", win_total)
    print("Lose: ", loss_total)
    print("-"*20)

    chance_to_win_percentage(games)
    visualize_chance_to_win()


def main():
    automatic_black_jack()


if __name__ == "__main__":
    main()