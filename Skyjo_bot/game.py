from action import choose_position, pick_deck, pick_discard
from deck import create_deck, create_discard_pile
from graphics import show_discard_pile, show_hand
from player import (
    calculate_score,
    create_players,
    has_hidden_cards,
    remove_identical_columns,
    reveal_first_cards,
)
from bot import choix_bot_action, choose_bot_position
from action import replace_card
from deck import take_card, take_discard_card
import random








def play_bot_turn(player, deck, discard_pile):
    """Fait jouer automatiquement le bot."""

    choice = choix_bot_action(discard_pile)

    row, column = choose_bot_position(player, prefer_hidden=choice == "1")

    if choice == "1":
        # Prendre la carte de la défausse
        card = take_discard_card(discard_pile)

        replace_card(
            player, card, discard_pile, row, column
        )

    else:
        # Piocher une carte
        card = take_card(deck)

        old_card = player["hand"][row][column]

        # On garde la carte si elle est meilleure
        if card["value"] < old_card["value"] and old_card["visible"]:
            replace_card(
                player, card, discard_pile, row, column
            )
        else:
            # Défausser la carte piochée
            card["visible"] = True
            discard_pile.append(card)

            # Retourner une carte cachée
            hidden = [
                (r, c)
                for r in range(3)
                for c in range(4)
                if (
                    player["hand"][r][c] is not None
                    and not player["hand"][r][c]["visible"]
                )
            ]

            if hidden:
                r, c = random.choice(hidden)
                player["hand"][r][c]["visible"] = True
            else:
                # Sans carte cachée, le bot doit
                # obligatoirement remplacer une carte
                # lorsqu'il pioche.
                discard_pile.pop()
                replace_card(
                    player, card, discard_pile, row, column
                )


























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
    removed_columns = remove_identical_columns(player)
    if removed_columns:
        print(f"Colonne(s) supprimée(s) : {', '.join(map(str, removed_columns))}")


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
        if player["name"] == 2:
            play_bot_turn(player, deck, discard_pile)
        else:
            play_bot_turn(player, deck, discard_pile)
        show_hand(players)
        show_discard_pile(discard_pile)

        if not has_hidden_cards(player):
            finished_player = current_player
            print(f"\nLe joueur {player['name']} n'a plus de cartes cachées.")

        current_player = (current_player + 1) % len(players)

    for _ in range(len(players) - 1):
        player = players[current_player]
        print(f"\nDernier tour du joueur {player['name']}")
        play_bot_turn(player, deck, discard_pile)
        removed_columns = remove_identical_columns(player)
        if removed_columns:
            print(f"Colonne(s) supprimée(s) : {', '.join(map(str, removed_columns))}")
        current_player = (current_player + 1) % len(players)

    show_scores(players)
    print("\nLa manche est terminée.")
