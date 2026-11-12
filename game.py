from action import choose_position, pick_deck, pick_discard
from deck import create_deck, create_discard_pile
from graphics import show_discard_pile, show_hand
from player import calculate_score, create_players, has_hidden_cards, reveal_first_cards


def choose_action():
    """Demande l'action du joueur."""
    while True:
        choice = input("1 - prendre la défausse, 2 - piocher : ")
        if choice in ("1", "2"):
            return choice
        print("Choisissez 1 ou 2.")


def play_turn(player, deck, discard_pile):
    """Fait jouer un joueur pendant un tour."""
    print(f"\nTour du joueur {player['name']}")
    show_hand([player])
    show_discard_pile(discard_pile)
    if choose_action() == "1":
        pick_discard(player, discard_pile)
    else:
        pick_deck(deck, player, discard_pile)


def show_scores(players):
    """Calcule et affiche le score final de chaque joueur."""
    print("\nScores :")
    for player in players:
        player["score"] = calculate_score(player)
        print(f"Joueur {player['name']} : {player['score']} points")


def run_game():
    """Initialise et lance une manche complète de Skyjo."""
    deck = create_deck()
    players = create_players(deck)

    for player in players:
        print(f"\nJoueur {player['name']}, choisissez vos deux cartes.")
        reveal_first_cards(player, choose_position)

    discard_pile = create_discard_pile(deck)
    current_player = 0
    finished_player = None

    while finished_player is None:
        player = players[current_player]
        play_turn(player, deck, discard_pile)
        show_hand(players)
        show_discard_pile(discard_pile)

        if not has_hidden_cards(player):
            finished_player = current_player
            print(f"\nLe joueur {player['name']} n'a plus de cartes cachées.")

        current_player = (current_player + 1) % len(players)

    for _ in range(len(players) - 1):
        player = players[current_player]
        print(f"\nDernier tour du joueur {player['name']}")
        pick_deck(deck, player, discard_pile)
        current_player = (current_player + 1) % len(players)

    show_scores(players)
    print("\nLa manche est terminée.")
