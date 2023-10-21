# Exercie-informatique
# Saisie du nombre de jours
nbj = int(input("Entrez le nombre de jours : "))

# Calcul des années, semaines et jours
annees = nbj // 365
nbj_restant = nbj % 365
semaines = nbj_restant // 7
jours = nbj_restant % 7

# Affichage du résultat
print(f"{nbj} jours équivalent à {annees} année(s), {semaines} semaine(s) et {jours} jour(s)")
