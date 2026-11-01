import random
from deck import deck, take_card
from player import create_player, reveal_first_cards
from graphics import show_hand, show_discard_pile
from action import pick_card

def has_hidden_cards(player):
    #Permet de verifier si un joueur à des cartes encore cacher
    for row in player["hand"]:
        for card in row:
            if not card["visible"]:
                return True
    return False


def create_game(deck):
    print("Bienvenue dans le jeu de Skyjo")
    players = create_player(deck)#Création des joueurs

    for player in players:#Fais retouner les 2 cartes du début à tout les joueurs
            print(f"Joueur {player['name']}, choisissez vos cartes à retourner")
            reveal_first_cards(player)
    show_hand(players)

    discard_pile = [take_card(deck)]
    discard_pile[0]["visible"] = True
    current_player = 0
    finished_player = None
    while finished_player is None:
        player = players[current_player]

        print(f"\nTour du joueur {player['name']}")
        pick_card(deck, player, discard_pile)
        show_hand(players)
        show_discard_pile(discard_pile)

        if not has_hidden_cards(player):
             finished_player = current_player
             print(f"Le joueur {player['name']} n'a plus de cartes cachées.")
        current_player = (current_player + 1) % len(players)
    for i in range(len(players) - 1):
        player = players[current_player]

        print(f"\nDernier tour du joueur {player['name']}")
        pick_card(deck, player, discard_pile)
        show_hand(players)

        current_player = (current_player + 1) % len(players)
    print("\nLa manche est terminée")

