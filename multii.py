import subprocess
import threading
import os

def generate_onion_link(prefix):
    process = subprocess.Popen(["oniongen", "^"+prefix, "5"], stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Erreur lors de la génération du lien onion : {error}")
    else:
        links = output.strip().decode().split('\n')
        for link in links:
            print(f"Lien onion généré : {link}")
            copy_key = input(f"Voulez-vous copier la clé privée dans /var/lib/tor/hidden_service/ ? (y/n)")
            if copy_key == 'y':
                key_path = "/var/lib/tor/hidden_service/"+link.replace(".onion","")
                if os.path.exists(key_path):
                    os.system(f"cp {key_path}/hs_ed25519_secret_key {key_path}/hs_ed25519_public_key {key_path}/hostname /var/lib/tor/hidden_service/")
                    os.system("chown -R debian-tor /var/lib/tor")
                    os.system("chmod 700 /var/lib/tor/hidden_service")
                    os.system("sudo /etc/init.d/tor restart")
                    os.system("sudo -u debian-tor tor")
                    print(f"Les clés privées ont été copiées dans {key_path}")
                else:
                    print(f"Impossible de trouver les clés privées dans {key_path}")

prefixes = ["anonym", "trhack", "trhacknn", "trh4ckn0", "trhack"]
threads = []

# lancer 5 threads pour générer des liens onion de vanité
for prefix in prefixes:
    thread = threading.Thread(target=generate_onion_link, args=(prefix,))
    thread.start()
    threads.append(thread)

# attendre la fin de tous les threads
for thread in threads:
    thread.join()
