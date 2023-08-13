import os
import subprocess
import threading

def generate_onion_address(prefix):
    # utiliser la commande oniongen pour générer une adresse onion avec le préfixe donné
    result = subprocess.run(["oniongen", f"^{prefix}", "5"], capture_output=True)
    stdout = result.stdout.decode().strip()
    if stdout:
        return stdout.split("\n")[0]
    else:
        return None

def generate_onion_addresses(prefixes):
    threads = []
    for prefix in prefixes:
        thread = threading.Thread(target=generate_onion_address, args=(prefix,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def copy_keys():
    copy = input("Voulez-vous sauvegarder /var/lib/tor/hidden_service et copier les cles dans /var/lib/tor/hidden_service? (y/n)")
    if copy == 'y':
        os.system("python3 cpkey.py")
    else:
        print("Aucune sauvegarde effectuée.")

# demander les préfixes à utiliser pour générer les adresses onion
prefixes = input("Entrez les préfixes à utiliser pour générer les adresses onion (séparés par des espaces) : ").split()
generate_onion_addresses(prefixes)
copy_keys()
