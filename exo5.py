import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
vitesse_inititale = int(input("Vitesse initiale (en m/s): "))

# Demander l'angle de lancement
angle_lancer = int(input("Angle de lancer (en degrés): "))

# Convertir l'angle en radians
angle_radians = (angle_lancer)*math.pi/180

# Calculer la distance maximale en x
distance_parcourue = f"{round((vitesse_inititale ** 2 * math.sin(2 * angle_radians)) / g, 2):.2f}"

# Afficher la distance maximale arrondie à 2 chiffres après la virgule
print(f"Distance parcourue: {distance_parcourue}m")