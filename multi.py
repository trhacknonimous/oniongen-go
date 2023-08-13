import subprocess
import threading
import os

def generate_onion_link(prefix):
    process = subprocess.Popen(["oniongen", "^"+prefix, "5"], stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Erreur lors de la génération du lien onion : {error}")
    else:
        link = output.strip().decode()
        print(f"Lien onion généré : {link}")
        copy_key = input(f"Voulez-vous copier la clé privée dans /var/lib/tor/hidden_service/ ? (y/n)")
        if copy_key == 'y':
            key_path = "/var/lib/tor/hidden_service/"+link.replace(".onion","")
            if os.path.exists(key_path):
                os.system(f"cp {key_path}/hs_ed25519_secret_key {key_path}/hs_ed25519_public_key {key_path}/hostname /var/lib/tor/hidden_service/")
                print(f"Les clés privée et publique ont été copiées dans /var/lib/tor/hidden_service/")
            else:
                print(f"Impossible de trouver la clé privée dans {key_path}")

prefixes = ["trhacknn", "trkn", "anonymous", "trh4ck", "trh4ck3r"]
threads = []

# lancer 5 threads pour générer des liens onion de vanité
for prefix in prefixes:
    thread = threading.Thread(target=generate_onion_link, args=(prefix,))
    thread.start()
    threads.append(thread)

# attendre la fin de tous les threads
for thread in threads:
    thread.join()
