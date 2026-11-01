import random
from deck import deck
from player import create_player, reveal_first_cards


def create_game(deck):
    print("Bienvenue dans le jeu de Skyjo")
    players = create_player(deck)#Création des joueurs
    for player in players:#Fais retouner les 2 cartes du début à tout les joueurs
        print(f"Joueur {player['name']}, choisissez vos cartes")
        reveal_first_cards(player)



create_game(deck)