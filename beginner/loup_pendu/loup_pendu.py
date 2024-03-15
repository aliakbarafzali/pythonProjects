import random


mots_possibles = [
    'python', 'ordinateur', 'programmation', 'clavier', 'souris',
    'écran', 'internet', 'livre', 'bibliothèque', 'café',
    'soleil', 'lune', 'étoile', 'planète', 'galaxie',
    'océan', 'montagne', 'rivière', 'désert', 'forêt',
    'chat', 'chien', 'oiseau', 'requin', 'tigre',
    'pomme', 'banane', 'orange', 'raisin', 'fraise',
    'voiture', 'avion', 'bicyclette', 'moto', 'bateau'
]

print("Bienvenue au jeu du Loup.")
print("1. Trouver un mot")
print("2. Jouer contre l'IA")
choice = input("Entrez votre sélection : ")

def remplace_lettre(chaine, index, nouveau_caractere):
    if isinstance(chaine, list):
        chaine[index] = nouveau_caractere
        return chaine
    else:       
        return chaine[:index] + nouveau_caractere + chaine[index + 1:]

def findWord():
    randomWord = random.choice(mots_possibles).lower()
    wordProgression = ['_'] * len(randomWord)
    tentatives = 0
    listeEssai = []

    while tentatives < 8 and '_' in wordProgression:
        print("\nVoici le mot à deviner : " + ' '.join(wordProgression))
        essai = input("Devinez une lettre ou tentez votre chance avec le mot entier : ").lower()

        if not essai.isalpha():
            print("Veuillez entrer uniquement des lettres.")
            continue

        if essai == randomWord:
            print("Félicitations! Vous avez correctement deviné le mot :", randomWord)
            return

        if len(essai) != 1:
            print("Veuillez entrer une seule lettre à la fois ou tenter de deviner le mot entier.")
            continue

        if essai in listeEssai:
            print("Vous avez déjà essayé cette lettre.")
            continue

        listeEssai.append(essai)
        if essai in randomWord:
            print("Vous avez eu juste!")
            for index, letter in enumerate(randomWord):
                if letter == essai:
                    wordProgression[index] = essai
        else:
            tentatives += 1
            print(f"Faux! Il vous reste {8 - tentatives} essais.")

    if '_' in wordProgression:
        print(f"Vous avez perdu! Le mot était : {randomWord}")
    else:
        print("Félicitations! Vous avez trouvé le mot :", ''.join(wordProgression))

    choice = input('Voulez-vous une autre partie ? O/N: ')
    if choice.upper() == "O":
        findWord()


    
if choice in ('1' ,'2'):
    if choice == '1':
        findWord()
    else:
        print("Cette fonctionnalité n'est pas encoré developpé! :) ")
else:
    print("Erreur, veuillez choisir une option dans le menu.")