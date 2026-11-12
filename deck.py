import random


def create_deck():
    """Crée une pioche complète de cartes Skyjo mélangées."""
    values = [-2] * 5 + [-1] * 10 + [0] * 15 + list(range(1, 13)) * 10
    random.shuffle(values)
    return values


def take_card(deck):
    """Retire et retourne la dernière carte de la pioche."""
    if not deck:
        raise ValueError("La pioche est vide.")

    return {"value": deck.pop(), "visible": False}


def create_discard_pile(deck):
    """Crée une défausse avec une carte visible."""
    card = take_card(deck)
    card["visible"] = True
    return [card]
