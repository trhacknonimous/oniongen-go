import os

def move_hidden_service():
    # demander si on veut déplacer le dossier /var/lib/tor/hidden_service
    move_dir = input("sauvegarde: Voulez-vous déplacer le dossier /var/lib/tor/hidden_service vers /var/lib/tor/hidden_service_ori? (y/n)")
    if move_dir == 'y':
        os.system("mv /var/lib/tor/hidden_service /var/lib/tor/hidden_service_ori")
        print("Dossier déplacé avec succès.")
    else:
        print("Aucun déplacement effectué.")

def copy_keys():
    current_directory = os.getcwd()
    # lister les dossiers présents dans le dossier courant
    dirs = [d for d in os.listdir(current_directory) if os.path.isdir(d)]
    if dirs:
        print("Liste des dossiers présents dans le dossier courant : ")
        for i, dir in enumerate(dirs):
            print(f"{i+1}. {dir}")
        # demander à l'utilisateur de choisir un dossier
        choice = input("Choisissez le dossier à partir duquel copier les clés : ")
        try:
            choice = int(choice)
            key_path = dirs[choice-1]
            if os.path.exists(key_path):
                os.system(f"cp {key_path}/hs_ed25519_secret_key {key_path}/hs_ed25519_public_key {key_path}/hostname /var/lib/tor/hidden_service/")
                os.system("chown -R debian-tor /var/lib/tor")
                os.system("chmod 700 /var/lib/tor/hidden_service")
                os.system("sudo /etc/init.d/tor restart")
                os.system("sudo -u debian-tor tor")
                print(f"Les clés privées ont été copiées dans /var/lib/tor/hidden_service/")
            else:
                print(f"Impossible de trouver les clés privées dans {key_path}")
        except ValueError:
            print("Entrée non valide.")

move_hidden_service()
copy_keys()
