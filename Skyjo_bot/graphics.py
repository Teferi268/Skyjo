def show_hand(players):
    for player in players:
        print(f"\nMain du joueur {player['name']} :")
        for row in player["hand"]:
            display_cards = []
            for card in row:
                if card is None:
                    display_cards.append("X")
                elif card["visible"]:
                    display_cards.append(str(card["value"]))
                else:
                    display_cards.append("?")
            print(" | ".join(display_cards))

def show_discard_pile(discard_pile):
    top_card = discard_pile[-1]
    print(f"\nDéfausse : {top_card['value']}")
