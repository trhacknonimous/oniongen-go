import os
from threading import Thread

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
