import random
from deck import deck
from player import create_player


def create_game(deck):
    print("Bienvenue dans le jeu de Skyjo")
    print(create_player(deck))


create_game(deck)