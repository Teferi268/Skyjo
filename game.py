import random
from deck import create_deck, deck
from player import create_player


def create_game(deck):
    print("Bienvenue dans le jeu de Skyjo")
    create_player()
    print(deck)

create_game(deck)