import random
from deck import deal_card, deck

def create_player(deck):
    nb_player = int(input("Combien de joueur êtes vous ?..."))
    players = []
    for i in range(nb_player):
        hand = []
        for row in range(3):
            current_row = []
        for column in range(4):
            current_row.append(deal_card(deck))
        hand.append(current_row)

    player = {
        "name": i + 1,
        "hand": hand,
        "score" : 0
    }
    players.append(player)
    return players

