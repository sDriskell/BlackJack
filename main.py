"""
Shane Driskell
Blackjack Simulator
Runs multiple hands of Blackjack to simulate chances to win with starting
hand versus the dealer.
"""
import random


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
        else:
            return points


#TODO: determine if player or dealer hit


#TODO: compare hands to see who wins


#TODO: Track win/losses


#TODO: Display win percentages


#TODO: Make manual Blackjack game


def automatic_black_jack():
    """Automatically run the game(s) and generate statistical data from it"""
    win_total = 0
    loss_total = 0
    temp_total = 0

    games_played_counter = 0

    results_table = [[0 for x in range(1, 11)] for y in range(1, 11)]

    player_hand = []
    dealer_hand = []

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

        player_hand.clear()
        dealer_hand.clear()


def main():
    automatic_black_jack()


if __name__ == "__main__":
    main()