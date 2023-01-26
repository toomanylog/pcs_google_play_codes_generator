import random
import string
import os
from datetime import datetime

# Choix du module par l'utilisateur
module = input("Choisissez un module (Google Play ou PCS): ")

# Nombre de codes générés par l'utilisateur
quantity = int(input("Choisissez un nombre de codes à générer: "))

# Longueur et format des codes pour chaque module
code_length = {
    "Google Play": 19,
    "PCS": 10
}
code_format = {
    "Google Play": [string.ascii_uppercase + string.digits, string.ascii_uppercase + string.digits, string.ascii_uppercase + string.digits, string.ascii_uppercase + string.digits, string.ascii_uppercase + string.digits],
    "PCS": string.ascii_uppercase + string.digits
}

# Générer un code aléatoire
def generate_code(module):
    if module == "Google Play":
        code = '-'.join(''.join(random.choice(characters) for _ in range(4)) for characters in code_format[module])
    else:
        code = ''.join(random.choice(code_format[module]) for _ in range(code_length[module]))
    return code

# Création du dossier pour stocker les résultats
if not os.path.exists(module):
    os.mkdir(module)

# Nom du fichier pour stocker les résultats
filename = f"{module}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
filepath = os.path.join(module, filename)

# Ecriture des résultats dans le fichier
with open(filepath, "w") as f:
    for i in range(quantity):
        code = generate_code(module)
        f.write(code + "\n")
        print(f"Code généré: {code}") # Affiche les codes générés en temps réel sur la console

print(f"Les codes ont été générés et enregistrés dans le fichier {filename}.")
