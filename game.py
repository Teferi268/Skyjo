import random
from deck import deck, take_card
from player import create_player, reveal_first_cards
from graphics import show_hand
from action import pick_card


def create_game(deck):
    print("Bienvenue dans le jeu de Skyjo")
    players = create_player(deck)#Création des joueurs

    for player in players:#Fais retouner les 2 cartes du début à tout les joueurs
            print(f"Joueur {player['name']}, choisissez vos cartes à retourner")
            reveal_first_cards(player)
    show_hand(players)

    discard_pile = [take_card(deck)]
    discard_pile[0]["visible"] = True
    
    print("Tour du joueur 1")
    pick_card(deck, players[0], discard_pile)
    
    show_hand(players)

