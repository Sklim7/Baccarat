import random
import csv

# Card deck values for Baccarat (Ace = 1, Face cards = 0)
CARD_VALUES = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 0, "J": 0, "Q": 0, "K": 0}


def draw_card():
    return random.choice(list(CARD_VALUES.keys()))


def calculate_hand_total(hand):
    return sum(CARD_VALUES[card] for card in hand) % 10


def baccarat_round():
    player_hand = [draw_card(), draw_card()]
    banker_hand = [draw_card(), draw_card()]

    player_total = calculate_hand_total(player_hand)
    banker_total = calculate_hand_total(banker_hand)

    # Player's third-card rule
    if player_total < 6:
        player_hand.append(draw_card())
        player_total = calculate_hand_total(player_hand)

    # Banker's third-card rule (dependent on player's third card if drawn)
    if banker_total < 3 or (banker_total == 3 and player_hand[-1] != "8") or \
            (banker_total == 4 and player_hand[-1] in ["2", "3", "4", "5", "6", "7"]) or \
            (banker_total == 5 and player_hand[-1] in ["4", "5", "6", "7"]) or \
            (banker_total == 6 and player_hand[-1] in ["6", "7"]):
        banker_hand.append(draw_card())
        banker_total = calculate_hand_total(banker_hand)

    if player_total > banker_total:
        result = "Player wins"
    elif banker_total > player_total:
        result = "Banker wins"
    else:
        result = "Tie"

    return [player_hand, player_total, banker_hand, banker_total, result]


#number of rounds can be modified
def simulate_baccarat(rounds=10000, filename="baccarat_results.csv"):
    results = []

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Player Hand", "Player Total", "Banker Hand", "Banker Total", "Result"])

        for _ in range(rounds):
            round_result = baccarat_round()
            results.append(round_result[-1])
            writer.writerow(round_result)



if __name__ == "__main__":
    simulate_baccarat()
