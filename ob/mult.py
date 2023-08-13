import os
from threading import Thread

def display_banner(text):
    color_code = '\033[1;%dm'
    reset_color = '\033[0m'
    colors = [31, 32, 33, 34, 35, 36]

    # Ajouter des bordures
    border_top = "+" + "-" * (len(text) + 2) + "+"
    border_bottom = "+" + "-" * (len(text) + 2) + "+"
    text_line = "| " + text + " |"

    # Ajouter des symboles décoratifs
    symbol_top = "/\\___/\\"
    symbol_bottom = "\\/   \\/"

    # Construire la bannière
    banner = ""
    banner += color_code % colors[0] + border_top + "\n"
    banner += color_code % colors[1] + symbol_top + " " * (len(text) - 4) + symbol_top + reset_color + "\n"
    banner += color_code % colors[2] + text_line + reset_color + "\n"
    banner += color_code % colors[3] + symbol_bottom + " " * (len(text) - 4) + symbol_bottom + reset_color + "\n"
    banner += color_code % colors[4] + border_bottom + reset_color

    print(banner)

# Afficher la bannière
display_banner('bruteforce ed25519')
display_banner('by Trhacknon')

def generate_onion_address(prefix, number_of_links):
    os.system(f"./oniongen ^{prefix} {number_of_links}")

def copy_keys():
    copy_keys = input("Voulez-vous sauvegarder /var/lib/tor/hidden_service et copier les clés dans /var/lib/tor/hidden_service? (y/n)")
    if copy_keys == 'y':
        os.system("python3 cpkey.py")
    else:
        print("Aucune copie de clé effectuée.")

prefixes = input("Entrez les préfixes à utiliser (séparés par des espaces) : ")
number_of_links = input("Entrez le nombre de liens à générer pour chaque préfixe : ")
number_of_threads = input("Entrez le nombre de threads à utiliser : ")

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
