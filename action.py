from deck import take_card


def choose_position(player, message):
    """Demande une position existante dans la main du joueur."""
    while True:
        try:
            row = int(input(f"{message} - ligne (1 à 3) : ")) - 1
            column = int(input("Colonne (1 à 4) : ")) - 1
            if 0 <= row < 3 and 0 <= column < 4:
                return row, column
        except ValueError:
            pass
        print("Cette position est invalide.")


def replace_card(player, card, discard_pile, row, column):
    """Remplace une carte de la main et place l'ancienne en défausse."""
    old_card = player["hand"][row][column]
    card["visible"] = True
    player["hand"][row][column] = card
    old_card["visible"] = True
    discard_pile.append(old_card)


def pick_discard(player, discard_pile):
    """Prend la carte visible de la défausse et la joue."""
    if not discard_pile:
        raise ValueError("La défausse est vide.")
    card = take_card(discard_pile)
    row, column = choose_position(player, "Position à remplacer")
    replace_card(player, card, discard_pile, row, column)


def pick_deck(deck, player, discard_pile):
    """Pioche une carte et laisse le joueur la jouer ou la défausser."""
    card = take_card(deck)
    print(f"Carte piochée : {card['value']}")

    while True:
        choice = input("1 - remplacer une carte, 2 - défausser : ")
        if choice in ("1", "2"):
            break
        print("Choisissez 1 ou 2.")

    if choice == "1":
        row, column = choose_position(player, "Position à remplacer")
        replace_card(player, card, discard_pile, row, column)
        return

    card["visible"] = True
    discard_pile.append(card)
    row, column = choose_position(player, "Carte cachée à retourner")
    player["hand"][row][column]["visible"] = True
