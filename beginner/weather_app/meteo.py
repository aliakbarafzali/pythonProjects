import requests

def obtenir_meteo(ville, cle_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={cle_api}&units=metric&lang=fr"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        donnees = reponse.json()
        temperature = donnees['main']['temp']
        description = donnees['weather'][0]['description']
        print(f"La température à {ville} est de {temperature}°C avec un ciel {description}.")
    else:
        print("Erreur dans la requête de données météo.")

def ville_la_plus_chaude(cle_api):
    # Logique pour déterminer la ville la plus chaude
    pass

def ville_la_plus_froide(cle_api):
    # Logique pour déterminer la ville la plus froide
    pass

def temperature_moyenne(cle_api):
    # Logique pour calculer la température moyenne
    pass

def menu_principal():
    cle_api = "c59ca7481e1d25c6f7f26a90c7406e01"  # Remplace cela par ta clé API réelle

    while True:
        print("""
Bienvenue dans l'application météo !
1. Avoir la météo d'une ville
2. La ville la plus chaude de France
3. La ville la plus froide de France
4. La température moyenne en France
5. Quitter""")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ville = input("Entrez le nom de la ville : ")
            obtenir_meteo(ville, cle_api)
        elif choix == "2":
            ville_la_plus_chaude(cle_api)
        elif choix == "3":
            ville_la_plus_froide(cle_api)
        elif choix == "4":
            temperature_moyenne(cle_api)
        elif choix == "5":
            print("Merci d'avoir utilisé l'application météo. À bientôt !")
            break
        else:
            print("Choix non valide. Veuillez entrer un numéro entre 1 et 5.")

if __name__ == "__main__":
    menu_principal()
