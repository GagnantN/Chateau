import time
import sys

def print_with_delay(text, delay = 0.03):
    for i in range(len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()
    

# Exercice 1 : créer une case (49)
# 1) créer une chaine de caractère pour representer la case (dessin)
# 2) découper chaque ligne en 4 ou 5, en chaine de caractere
# 3) créer une boucle qui print chacune de ces lignes
# 4) vériier que l'affichage de la boucle est identique à l'affichage souhaité.


# lignetotal.append(lines1)


# 5) créer l'image située a droite sous forme de tableau de ligne


# lignetotal.append(lines1 +lines2)

# 6) créer un tableau de ligne qui assemble la ligne 1 et 2
# lignetotal = list(zip(lines1,lines2))

# 7) créer une boucle qui affiche chacune des lignes


# map_line = []
# for i in range(len(lines1)):
#     map_line.append(lines1[i]+lines2[i])

# print(map_line)

# for line in map_line:
#     print(line)

# 8) créer un tableau de case.
game_map = [
    {
        "message" :"Vous êtes dans la hutte du sorcier du village. Il vous regarde avec des yeux ébènes et vous dit en riant : Bonjour mon bon roi, que puis-je faire pour vous ?",
        "haut": None,
        "bas": 9,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "         ",
            " Sorcier ",
        ],
        "occupe": False,
        "case_occupe": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "    R    ",
            " Sorcier ",
        ]
    },

    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "message" :"Bienvenue chez ce pouilleux de Paysan, il vous regarde avec un filet de bave coulant sur le coin droit de sa lèvre et vous dis en postillonant :  Bonzou ! Zeigneur z'ai un truc pour vouz !",
        "haut": None,
        "bas": 12,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "         ",
            "  Paysan ",
        ],
        "occupe": False,
        "case_occupe": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "    R    ",
            "  Paysan ",
        ]
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "         ",
            "   /\    ",
            "  /__\   ",
            "   ||    ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "       | ",
            "   /\    ",
            "  /__\ | ",
            "   ||  | ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "message" :"Bienvenue dans votre résidence tertiaire, je crois qu'en déménageant vous avez laisser un idice du mot-de-passe pour vous, voulez-vous le chercher ?",
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": 7,
        "case_vide": [
            "  []___  ",
            " /__ __\ ",
            " |___|_| ",
            "         ",
            "  Manoir ",
        ],
        "occupe": False,
        "case_occupe": [
            "  []___  ",
            " /__ __\ ",
            " |___|_| ",
            "    R    ",
            "  Manoir ",
        ]
    },
    {
        "message" :"Vous êtes à l'impasse du village, voulez-vous aller à droite vers l'église ? Où bien à gauche dans votre vieux manoir ?",
        "haut": None,
        "bas": 16,
        "gauche": 6,
        "droite": 8,
        "case_vide": [
            "         ",
            "_________",
            "___   ___",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "_________",
            "___ R ___",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "message" :"Bienvenue au coeur du village dans l'église de Soeur André, elle vous regarde avec un sourire miellieux et un calme verdoyant : Bienvenue mon seigneur dans la maison de Dieu. En quoi son humble servante pourrait-elle vous aider ?",
        "haut": None,
        "bas": None,
        "gauche": 7,
        "droite": None,
        "case_vide": [
            "  ___/ \ ",
            " /_____| ",
            " |___|_| ",
            "         ",
            " Eglise  ",
        ],
        "occupe": False,
        "case_occupe": [
            "  ___/ \ ",
            " /_____| ",
            " |___|_| ",
            "    R    ",
            " Eglise  ",
        ]
    },
    {
        "message" :"Vous êtes actuellement devant la maison du sorcier, je crois qu'il a un indice pour vous, voulez-vous le rencontrer ?",
        "haut": 0,
        "bas": None,
        "gauche": None,
        "droite": 10,
        "case_vide": [
            "   | |   ",
            "   | |___",
            "   |_____",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "   |R|___",
            "   |_____",
            "         ",
            "         ",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": None,
        "bas": None,
        "gauche": 9,
        "droite": 11,
        "case_vide": [
            "         ",
            "_________",
            "_________",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "_________",
            "____R____",
            "         ",
            "         ",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": None,
        "bas": None,
        "gauche": 10,
        "droite": 12,
        "case_vide": [
            "         ",
            "_________",
            "_________",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "_________",
            "____R____",
            "         ",
            "         ",
        ]
    },
    {
        "message": "En haut vous trouverez le paysan, à gauche ce trouve la hutte du sorcier.",
        "haut": 3,
        "bas": 21,
        "gauche": 11,
        "droite": None,
        "case_vide": [
            "   | |   ",
            "___| |   ",
            "___  |   ",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "___| |   ",
            "___ R|   ",
            "   | |   ",
            "   | |   "
        ]
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "         ",
            "   /\    ",
            "  /__\   ",
            "   ||    ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "message": "Bienvenu chez le Bucheron, je crois qu'il est instable, méfiez-vous.. ",
        "haut": None,
        "bas": 23,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "         ",
            " Bucheron",
        ],
        "occupe": False,
        "case_occupe": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "    R    ",
            " Bucheron",
        ]
    },
    {
        "message": "Une maison abandonnée, rien d'intéressant",
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": 16,
        "case_vide": [
            "   ___   ",
            "  /___\  ",
            "  |[]_|  ",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "    R    ",
            "         ",
        ]
    },
    {
        "message": "Vous êtes au centre du village.",
        "haut": 7,
        "bas": 25,
        "gauche": 15,
        "droite": 17,
        "case_vide": [
            "   | |   ",
            "___| |___",
            "___   ___",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "___| |___",
            "___ R ___",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "message": "Bienvenue chez le forgeron, sourd comme un pôt, à force de taper comme un hystérique sur l'enclume.",
        "haut": None,
        "bas": None,
        "gauche": 16,
        "droite": None,
        "case_vide": [
            "   _____ ",
            "  /___  |",
            "  |[  ]_|",
            "         ",
            " Forgeron",
        ],
        "occupe": False,
        "case_occupe": [
            "   _____ ",
            "  /___  |",
            "  |[  ]_|",
            "    R    ",
            " Forgeron",
        ]
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            ".[].     ",
            "|  |_____",
            "|[]|_____",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "message": "Vous êtes devans un étragne château, il se peut que ce soit le vôtre. Que voulez-vous faire ?",
        "haut": None,
        "bas": 28,
        "gauche": None,
        "droite": None,
        "case_vide": [
            ".[]. ____",
            "|  |/____",
            "|[]|___[ ",
            "         ",
            " Château ",
        ],
        "occupe": False,
        "case_occupe": [
            ".[]. ____",
            "|  |/____",
            "|[]|___[ ",
            "     R   ",
            " Château ",
        ]
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "____ .[].",
            "____\|  |",
            " ]___|[]|",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "message": "Continuez votre chemin.",
        "haut": 12,
        "bas": None,
        "gauche": None,
        "droite": 22,
        "case_vide": [
            "   | |   ",
            "   | |___",
            "   |_____",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "   | |___",
            "   |R____",
            "         ",
            "         ",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": None,
        "bas": 31,
        "gauche": 21,
        "droite": 23,
        "case_vide": [
            "         ",
            "_________",
            "___   ___",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "_________",
            "___ R ___",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "message": "Vous vous situez devans la cabane du Bucheron, éteignez votre cigarette au cas où.",
        "haut": 14,
        "bas": None,
        "gauche": 22,
        "droite": None,
        "case_vide": [
            "   | |   ",
            "___| |   ",
            "_____|   ",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "___| |   ",
            "____R|   ",
            "         ",
            "         ",
        ]
    },
    {
        "message": "Vous êtes dans l'hôpital, vous pouvez voir de temps en temps Soeur André rôder autour des patients.",
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": 25,
        "case_vide": [
            "  []___  ",
            " /__ __\ ",
            " |__[]_| ",
            "         ",
            " Hopital ",
        ],
        "occupe": False,
        "case_occupe": [
            "  []___  ",
            " /__ __\ ",
            " |__[]_| ",
            "    R    ",
            " Hopital ",
        ]
    },
    {
        "message": "Vous êtes à l'entrée du village.",
        "haut": 16,
        "bas": 34,
        "gauche": 24,
        "droite": 26,
        "case_vide": [
            "   | |   ",
            "___| |___",
            "___   ___",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "___| |___",
            "___ R ___",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "message": "Vous trouvez la fillette du Boucher entrain de ramasser un bout de viande qui semble ressembler à un doigt.",
        "haut": None,
        "bas": None,
        "gauche": 25,
        "droite": None,
        "case_vide": [
            "   _____ ",
            "  /___  |",
            "  |[/\]_|",
            "         ",
            " Boûcher ",
        ],
        "occupe": False,
        "case_occupe": [
            "   _____ ",
            "  /___  |",
            "  |[/\]_|",
            "     R   ",
            " Boûcher ",
        ]
    },
    {
        "message": "Voulez-vous entrer dans la cabane abandonnée.",
        "haut": None,
        "bas": 36,
        "gauche": None,
        "droite": 28,
        "case_vide": [
            "         ",
            "    _____",
            "   |  ___",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "    _____",
            "   |R ___",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": 19,
        "bas": 37,
        "gauche": 27,
        "droite": 29,
        "case_vide": [
            "   | |   ",
            "___| |___",
            "___   ___",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "___| |___",
            "___ R ___",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": None,
        "bas": 38,
        "gauche": 28,
        "droite": None,
        "case_vide": [
            "         ",
            "_____    ",
            "___  |   ",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "_____    ",
            "___ R|   ",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "message": "Continuez votre chemin.",
        "haut": 22,
        "bas": 40,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "   | |   ",
            "   | |   ",
            "   | |   ",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "   | |   ",
            "   |R|   ",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "         ",
            "         ",
            "         ",
            "         ",
            "         ",
        ],
        "occupe": False,
        "case_occupe": None
    },
    {
        "message": "Continuez votre chemin, le village est devans vous.",
        "haut": 25,
        "bas": 43,
        "gauche": None,
        "droite": 35,
        "case_vide": [
            "   | |   ",
            "   | |__ ",
            "   |  __ ",
            "   | |   ",
            "   | |   ",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "   | |__ ",
            "   |R __ ",
            "   | |   ",
            "   | |   ",
        ]
    },
    {
        "message": "Vous êtes devant le gardien du village. Son ronfflement en dit long sur son travail...",
        "haut": None,
        "bas": None,
        "gauche": 34,
        "droite": None,
        "case_vide": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "         ",
            " Gardien ",
        ],
        "occupe": False,
        "case_occupe": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "    R    ",
            " Gardien ",
        ]
    },
    {
        "message": "Vous êtes dans une maison délabré ou gis devant vous un papier déchiré.",
        "haut": 27,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "         ",
            "_________",
        ],
        "occupe": False,
        "case_occupe": [
            "   ___   ",
            "  /  _\  ",
            "  |_|_|  ",
            "    R    ",
            "_________",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": 28,
        "bas": None,
        "gauche": None,
        "droite": 38,
        "case_vide": [
            "   | |   ",
            "   | |___",
            "   |_____",
            "         ",
            "_________",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "   | |___",
            "   |R____",
            "         ",
            "_________",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": 29,
        "bas": None,
        "gauche": 37,
        "droite": 39,
        "case_vide": [
            "   | |   ",
            "___| |___",
            "_________",
            "         ",
            "_________",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "___| |___",
            "____R____",
            "         ",
            "_________",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": None,
        "bas": None,
        "gauche": 38,
        "droite": 40,
        "case_vide": [
            "         ",
            "_________",
            "_________",
            "         ",
            "_________",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "_________",
            "____R____",
            "         ",
            "_________",
        ]
    },
    {
        "message": "Vous êtes à l'entrée de votre territoire, face à vous se trouve la campagne, à gauche votre château et à droite le village.",
        "haut": None, #31,
        "bas": None,
        "gauche": 39,
        "droite": None, #41,
        "case_vide": [
            "   | |   ",
            "___| |___",
            "___   ___",
            "   | |   ",
            "___| |___",
        ],
        "case_occupe": [
            "   | |   ",
            "___| |___",
            "___ R ___",
            "   | |   ",
            "___| |___",
        ],
        "occupe": True,
        "case_bloque_occupe": [
            "   |_|   ",
            "___| |___",
            "___ R _|_",
            "   | |   ",
            "___| |___",
        ],
        "case_bloque_vide": [
            "   |_|   ",
            "___| |___",
            "___   _|_",
            "   | |   ",
            "___| |___",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": None,
        "bas": None,
        "gauche": 40,
        "droite": 42,
        "case_vide": [
            "         ",
            "_________",
            "_________",
            "         ",
            "_________",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "_________",
            "____R____",
            "         ",
            "_________",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": None,
        "bas": None,
        "gauche": 41,
        "droite": 43,
        "case_vide": [
            "         ",
            "_________",
            "_________",
            "         ",
            "_________",
        ],
        "occupe": False,
        "case_occupe": [
            "         ",
            "_________",
            "____R____",
            "         ",
            "_________",
        ]
    },
    {
        "message": "Continuez votre chemin.",
        "haut": 34,
        "bas": None,
        "gauche": 42,
        "droite": None,
        "case_vide": [
            "   | |   ",
            "___| |   ",
            "_____|   ",
            "         ",
            "_________",
        ],
        "occupe": False,
        "case_occupe": [
            "   | |   ",
            "___| |   ",
            "____R|   ",
            "         ",
            "_________",
        ]
    },
    {
        "haut": None,
        "bas": None,
        "gauche": None,
        "droite": None,
        "case_vide": [
            "         ",
            "         ",
            "         ",
            "         ",
            "_________",
        ],
        "occupe": False,
        "case_occupe": None,
    }   
]

# 9) créer deux objets avec une propriété case vide dont la valeur sont : les tableaux lines1 et lines2.


# 10) créer une boucle qui parcour le tableau de case, assemble chacune des lignes et affiche

nb_case_line = 5
nb_colonnes = 9
nb_lignes = 5
chateau_visite = False


def generer_map():
    map_view = []
    for i in range(nb_lignes):
        map_view.append([])
        for j in range(nb_case_line):
            line = "| " # Bordures gauche de la map.
            for k in range(nb_colonnes):
                en_cours = game_map[i*nb_colonnes+k]
                if chateau_visite == True: # Si le chateau est visité, accès à toute la map :
                    if en_cours["occupe"]: # La case actuelle est occupé :
                        line = line + en_cours["case_occupe"][j] # Carte affichée avec le "R".
                    else:
                        line = line+en_cours["case_vide"][j] # La case actuelle est non-occupé : Carte affichée sans le "R".
                else: # Si le chateau n'a pas été visité, accès restreint :
                    if en_cours["occupe"]: # Case actuelle occupé :
                        if "case_bloque" in en_cours.keys() and chateau_visite == False : # Bloquée ou pas ? 
                            line = line + en_cours["case_bloque_occupe"][j] # 'OUI' => Je suis sur une case bloqué et occupé : Carte affichée avec le "R".
                        else:
                            line = line + en_cours["case_occupe"][j]  # 'NON'=> Afficher la case non-bloqué et occupé : Carte affichée avec le "R".
                    else:
                        if "case_bloque" in en_cours.keys() and chateau_visite == True: # Bloqué ou pas ?
                            line = line + en_cours["case_bloque_vide"][j] # 'OUI'=> Je suis sur une case bloqué et non-occupé : Carte affichée sans le "R".
                        else:
                            line = line+en_cours["case_vide"][j] # 'NON', afficher la case non bloqué, non-occupé : Carte affichée sans le "R".
            line += " |" # Bordure droite de la map.
            map_view[i].append(line)
        
    sep = "__"
    for i in range(nb_colonnes*9):
        sep += "_"
    sep += "__"
    print(sep)
    
    return map_view


# create_map = generer_map() #Appeler la fonction

# 14) Créer une fonction qui affiche une liste de ligne
def affiche_map(map_view):
    for line in map_view:
        for case_line in line:
            print(case_line)

# affiche_map(create_map)
    
# 15) Créer une fonction qui prend une case en parametre, affiche les messages liés à la case et retourne la destination
def demander_choix(case):
    print_with_delay(case["message"])

    print_with_delay("Où voulez vous aller ?")
    if case["haut"] is not None :
        print_with_delay("- " + "haut")
    if case["bas"] is not None :
        print_with_delay("- " + "bas")
    if case["gauche"] is not None :
        print_with_delay("- " + "gauche")
    if case["droite"] is not None :
        print_with_delay("- " + "droite") 
    print()
    
    choice_utilisateur = input("Votre choix : ")
    return choice_utilisateur
        

        
# position_actuelle = game_map[40]
# choice = demander_choix(position_actuelle)



# 16) Créer une fonction qui prend un choix et la case en cours et qui retourne la case suivante. Si la case n'existe pas : retourne la case en cours. 

def mouvement(choice_utilisateur, case_actuelle) :
    autoriser = ["haut", "bas", "gauche", "droite"]
    if choice_utilisateur in autoriser and case_actuelle[choice_utilisateur]  is not None :
        case_actuelle["occupe"] = False
        case_actuelle = game_map[case_actuelle[choice_utilisateur]]
        case_actuelle["occupe"] = True
    else :
        print_with_delay("Impossible : veuillez réessayer")
        time.sleep(1.5)
    return case_actuelle

# i =0
# while i<100 : 
#     position_actuelle = mouvement(choice, position_actuelle)
#     affiche_map(generer_map())
#     choice = demander_choix(position_actuelle)
#     i += 1
    


# 17) Créer une fonction demarrage du jeu avec le droit de n'allez qu'à gauche

# ---------------- print_with_delay("Nous avons besoin d'aide, ça majesté est resté trop longtemps dans un casino et maintenant il doit rentrer chez lui au château. Aidez-le !")
time.sleep(1.5)

create_map = generer_map() #Appeler la fonction
affiche_map(create_map)
position_actuelle = game_map[40]
choice = demander_choix(position_actuelle)

for l in range(5) :  # Après 5 erreurs fin du jeu
    if l < 5 : 
        if choice == "gauche" :
            i =0
            while i<100 : 
                position_actuelle = mouvement(choice, position_actuelle)
                affiche_map(generer_map())
                choice = demander_choix(position_actuelle)
                i += 1

        else :
            print_with_delay("Vous n'avez pas l'autorisation d'y accéder")
    
    else :
        print_with_delay("Le jeu est terminé !!")