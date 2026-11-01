import random

def create_deck():
    return [-2] * 5 + [0] * 15 + list(range(1, 13)) * 10 + [-1] * 10

deck = create_deck()
random.shuffle(deck)
