import os
from threading import Thread
import questionary
from colorama import init, Fore
import random

# Initialisation de Colorama
init(autoreset=True)

# Fonction pour générer une couleur aléatoire
def random_color():
    return random.choice([Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.BLUE])

# Fonction pour générer une adresse Onion
def generate_onion_address(prefix, number_of_links):
    os.system(f"./oniongen ^{prefix} {number_of_links}")

# Fonction pour copier les clés
def copy_keys():
    copy_keys = questionary.confirm("Voulez-vous sauvegarder /var/lib/tor/hidden_service et copier les clés dans /var/lib/tor/hidden_service?").ask()
    if copy_keys:
        os.system("python3 cpkey.py")
    else:
        print(random_color() + "Aucune copie de clé effectuée.")

# Interface utilisateur
prefixes = questionary.text(random_color() + "Entrez les préfixes à utiliser (séparés par des espaces) :").ask()
number_of_links = questionary.text(random_color() + "Entrez le nombre de liens à générer pour chaque préfixe :").ask()
number_of_threads = questionary.text(random_color() + "Entrez le nombre de threads à utiliser :").ask()

prefixes = prefixes.split(" ")

threads = []
for prefix in prefixes:
    for i in range(int(number_of_threads)):
        t = Thread(target=generate_onion_address, args=(prefix, number_of_links))
        t.start()
        threads.append(t)
        
for t in threads:
    t.join()

copy_keys()