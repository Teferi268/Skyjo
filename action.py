import random
from deck import deck, take_card
from player import create_player, reveal_first_cards
from graphics import show_hand

def choice_card_to_replace(player,card,discard_pile):
    row = int(input("Ligne 1 à 3...")) -1
    column = int(input("Colonne 1 à 4...")) -1

    old_card = player["hand"][row][column]

    card["visible"] = True
    player["hand"][row][column] = card

    old_card["visible"] = True
    discard_pile.append(old_card)

def pick_card(deck,player, discard_pile):
    #Tirer une carte du deck
    card = take_card(deck)
    print(f"Voici la carte : {card['value']}")
    choice = int(input("1- remplacer un carte 2- défausser la carte tiré"))
    if choice == 1:
        choice_card_to_replace(player, card, discard_pile)
    elif choice == 2:
        card["visible"] = True
        discard_pile.append(card)

        row = int(input("Quelle carte cachée retourner ? Ligne : ")) - 1
        column = int(input("Colonne : ")) - 1
        player["hand"][row][column]["visible"] = True
