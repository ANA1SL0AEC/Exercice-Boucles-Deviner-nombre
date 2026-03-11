#Exercice d'entraînement : coder un petit programme m'exercant aux boucles :

import random

nombre_secret = random.randint(0,50)

guess = int(input("A quel nombre que je pense ? De 0 à 50 inclus !"))

while guess != nombre_secret :
    if guess < nombre_secret : 
        print("C'est plus grand biensûr !")
    elif guess > nombre_secret :
        print("C'est plus petit voyons !")

    guess = int(input("Essaie encore :"))

print("Bravo, je pensais bien à", nombre_secret)