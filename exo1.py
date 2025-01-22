from datetime import datetime

# Demander le nom complet de l'utilisateur
nom=str(input("Veuillez entrer votre nom complet : "))

# Demander l'âge de l'utilisateur
age_str=str(input("Veuillez entrer votre âge : "))
age = int(age_str)

# Définir l'année actuelle
DATE = datetime.today().year

# Calculer l'année de naissance
naissance=DATE-age

# Afficher un message de bienvenue avec le nom complet
print(f"Bonjour {nom}")

# Afficher l'année de naissance
print(f"Vous êtes né(e) en {naissance}")