import random

def  choix_bot_action(discard_pile):
    #Permet au bot de prendre la carte de la defausse si elle est inferieur à 3, sinon il pioche
    top_card = discard_pile[-1]["value"]
    if top_card <= 3:
        return "1"
    else: 
        return "2"

def choose_bot_position(player, prefer_hidden=False):
    # Le bot choisit une carte cachée lorsqu'il prend la défausse.
    hand = player["hand"]

    hidden_positions = [
        (row, column)
        for row in range(3)
        for column in range(4)
        if hand[row][column] is not None and not hand[row][column]["visible"]
    ]
    if prefer_hidden and hidden_positions:
        return random.choice(hidden_positions)

    best_position = None
    highest_value = float(-10000)
    for row in range(3):
        for column in range(4):
            card = hand[row][column]

            if card is not None and card["visible"]:
                if card["value"] > highest_value:
                    highest_value = card["value"]
                    best_position = (row, column)

    if best_position is not None:
        return best_position
    
    positions = [
        (r, c)
        for r in range(3)
        for c in range(4)
        if hand[r][c] is not None
    ]

    return random.choice(positions)