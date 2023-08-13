import zlib
import base64
import os

def obfuscate_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    obfuscated_code = base64.b85encode(zlib.compress(code.encode())).decode()
    obfuscated_code = f'import zlib, base64; exec(zlib.decompress(base64.b85decode(\'{obfuscated_code}\')).decode())'

    obfuscated_file_path = os.path.join('ob', os.path.basename(file_path))
    with open(obfuscated_file_path, 'w') as file:
        file.write(obfuscated_code)

    print(f'Obfuscated file {file_path} saved as {obfuscated_file_path}')

# Créer le répertoire 'ob' s'il n'existe pas déjà
os.makedirs('ob', exist_ok=True)

# Obfusquer tous les fichiers .py dans le répertoire actuel
for file_name in os.listdir('.'):
    if file_name.endswith('.py') and file_name != 'ob.py':
        obfuscate_file(file_name)
