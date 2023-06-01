import random

# Define the deck as a dictionary of card types and their respective counts
deck = {
    "Engine": 20,
    "Non Engine": 10,
    "Bricks": 10,
    # Add more card types and counts here
}

def simulate(deck, num_simulations):
    card_count = {card_type: 0 for card_type in deck}
    total_cards = sum(deck.values())
    total_cards_drawn = 5 * num_simulations

    for _ in range(num_simulations):
        # Draw a hand of 5 cards
        hand = random.choices(
            population=list(deck.keys()),
            weights=list(deck.values()),
            k=5
        )

        # Count the card types in the hand
        for card_type in hand:
            card_count[card_type] += 1

    # Print the percentages of each card type
    for card_type, count in card_count.items():
        percentage = (count / total_cards_drawn) * 100
        print(f"{card_type}: {percentage:.2f}%")

# Run the simulation with 10,000 iterations
simulate(deck, 10000)
