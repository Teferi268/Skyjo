from deck import take_card


ROWS = 3
COLUMNS = 4


def ask_player_count():
    """Demande un nombre de joueurs valide."""
    while True:
        try:
            count = int(input("Combien de joueurs êtes-vous ? "))
            if count >= 2:
                return count
        except ValueError:
            pass
        print("Veuillez choisir au moins 2 joueurs.")


def create_hand(deck):
    """Distribue une main de 12 cartes à un joueur."""
    return [
        [take_card(deck) for _ in range(COLUMNS)]
        for _ in range(ROWS)
    ]


def create_players(deck):
    """Crée les joueurs et leur distribue une main."""
    count = ask_player_count()
    return [
        {"name": number, "hand": create_hand(deck), "score": 0}
        for number in range(1, count + 1)
    ]


def reveal_first_cards(player, choose_position):
    """Retourne les deux cartes choisies au début de la manche."""
    for _ in range(2):
        row, column = choose_position(player, "Carte à retourner")
        player["hand"][row][column]["visible"] = True


def has_hidden_cards(player):
    """Indique si la main contient encore une carte cachée."""
    return any(
        not card["visible"]
        for row in player["hand"]
        for card in row
    )


def calculate_score(player):
    """Calcule le score actuel d'un joueur."""
    return sum(
        card["value"]
        for row in player["hand"]
        for card in row
    )
