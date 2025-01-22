secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees, secondes = divmod(secondes, 31536000)

# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
semaines, secondes = divmod(secondes, 604800)

# TODO: Assigner à la variable "jours" le nombre de jours restants
jours, secondes = divmod(secondes, 86400)

# TODO: Assigner à la variable "heures" le nombre d'heures restantes
heures, secondes = divmod(secondes, 3600)

# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
minutes, secondes = divmod(secondes, 60)

# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
print(annees, semaines, jours, heures, minutes, secondes)