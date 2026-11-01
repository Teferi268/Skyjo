import random
from deck import deck
from player import create_player, reveal_first_cards
def show_hand(players):
    for player in players:
        print(f"\nMain du joueur {player['name']} :")
        for row in player["hand"]:
            display_cards = []
            for card in row:
                if card["visible"]:
                    display_cards.append(str(card["value"]))
                else:
                    display_cards.append("?")
            print(" | ".join(display_cards))
    