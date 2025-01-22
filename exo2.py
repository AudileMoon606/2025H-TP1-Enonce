# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
pourcentage_str=str(input("Entrez le niveau de charge actuel de la batterie : "))
pourcentage=int(pourcentage_str)

# Vérifiez si le niveau de charge est valide
if pourcentage not in range (0, 101):
    print("Erreur : niveau de charge invalide.")
else:
    # Arrondir le pourcentage à la dizaine la plus proche
    pourcentage_arrondi = round(pourcentage,-1)
     
    # Calculer le nombre de barres
    barres=int(pourcentage_arrondi/10)

    # Afficher la représentation graphique de la charge de la batterie
    print(f"[{"❚"*barres+" "*(10-barres)}]")
    print(f"{pourcentage}%")