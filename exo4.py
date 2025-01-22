secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees = int(secondes/31536000)

# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
secondes_restantes = secondes-annees*31536000
semaines = int(secondes_restantes/604800)

# TODO: Assigner à la variable "jours" le nombre de jours restants
secondes_restantes = secondes_restantes - semaines*604800
jours = int(secondes_restantes/86400)

# TODO: Assigner à la variable "heures" le nombre d'heures restantes
secondes_restantes = secondes_restantes - jours*86400
heures = int(secondes_restantes/3600)

# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
secondes_restantes = secondes_restantes - heures*3600
minutes = int(secondes_restantes/60)

# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
secondes = secondes_restantes - minutes*60

# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
print(annees, semaines, jours, heures, minutes, secondes)