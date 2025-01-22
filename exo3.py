import math

a = int(input("Entrez a, non nul: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

# Calculer le discriminant et assigner la valeur dans la variable "delta"
delta = b**2 - 4*a*c

# Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
aUneSeuleSolution=False
if delta < 0 :
    naPasDeSolution = True
else : 
    naPasDeSolution = False
    if delta == 0:
        aUneSeuleSolution=True


if naPasDeSolution:
    print("Aucune racine")

elif aUneSeuleSolution:
    print("Une seule racine")
    x1 = (-b+math.sqrt(delta))/2*a
    print(x1)
    
else:
    print("Deux racines")
    x1 = (-b-math.sqrt(delta))/2*a
    x2 = (-b+math.sqrt(delta))/2*a
    print(x1,x2)