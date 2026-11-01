Jeu Skyjo en python


Regle du jeu :
    -Chaque joueur reçoit 12 cartes, 4 colonnes de 3 cartes
    -Chacun retourne 2 cartes de son choix 
    -Le reste forme une pioche et 1 carte est retouné pour former la défausse
    -Le joueur dont la somme des deux cartes visible est la plus élevé commence
    -Le joueur ayant le moins de point a la fin de la partie gagne
    

    -Deroulement d'un tour:
        -Prendre la carte visible de la défausse
            ->Tu remplaces obligatoirement une de tes cartes visible ou cachée. Tu poses la nouvelle face visible et tu défausses l’ancienne.
        -Piocher une carte cachée
            ->Tu la regardes, puis tu la gardes pour remplacer une de tes cartes
            ->ou tu la défausses et retournes obligatoirement une de tes cartes cachées.
        -Si aucune carte n'est cachée, les autres joueurs jouent encore un dernier tour et la partie s'arrete

    Regle spécial:
        -Si 3 cartes d'une même colonne sont visible et identique, on retire tout la colonne


Composition du jeu de carte:
    Le Skyjo classique contient 150 cartes, numérotées de -2 à 12:

    - 5 cartes de valeur -2.
    - 15 cartes de valeur 0.
    - 10 cartes de chaque valeur pour -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 et 12.

    