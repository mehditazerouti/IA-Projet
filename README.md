# IA-Projet
Voyageur de commerce avec les algorithmes génétiques
Implémentation
Les villes  :
J’itére sur M individus et pour chaque individu, j’ai générer N gènes (ou villes) avec des valeurs aléatoires et sans répétition 
J'ai utilisé la bibliothèque NumPy pour générer aléatoirement les coordonnées (x, y) des villes dans un espace bidimensionnel.
L'utilisateur peut spécifier le nombre de villes à générer via une interface graphique.
Algorithme génétique : 
J'ai implémenté les composantes principales de l'algorithme génétique (5 grandes étapes), notamment la population initiale, la sélection des parents, le croisement (crossover) et la mutation, ainsi que le calcul de la fitness pour évaluer la qualité de chaque individu pour créer de nouveaux individus et les Ajoutes dans la population
Création de la population initiale : 
J'ai initialisé une population d'individus, chacun représentant un chemin à travers les villes. J'ai utilisé une approche aléatoire pour générer les individus de la population initiale tout en évitant les redondances de villes dans un même chemin.
Evaluation de la "fitness" (qualité) des individus : 
J'ai passé à l'étape d'évaluation de la fitness des individus, une étape cruciale dans un algorithme génétique. À ce stade, j'ai évalué à quel point chaque individu dans la population est adapté au problème que je tente de résoudre, dans ce cas, le problème du voyageur de commerce.
Pour évaluer la fitness de chaque individu, j'ai calculé la longueur totale du parcours représenté par cet individu. Dans le TSP, cela signifie calculer la somme des distances entre chaque paire de villes dans le parcours, en tenant compte de l'ordre dans lequel les villes sont visitées.
Sélection des parents : 
La sélection des parents consiste à choisir les individus de la population actuelle qui seront utilisés pour produire la prochaine génération d'individus. Ces individus sélectionnés seront les "parents" qui contribueront à la reproduction pour créer de nouveaux individus.
Il existe plusieurs approches pour sélectionner les parents dans un algorithme génétique. 
Dans mon cas, j'ai opté pour une méthode basée sur la fitness des individus. Avant de sélectionner les parents, j'ai tout d'abord ordonné la population en fonction de la fitness de chaque individu, c'est-à-dire la distance totale parcourue. Cette étape m'a permis d'identifier les individus les plus performants en termes de distance minimale parcourue.
Ensuite, j'ai sélectionné les parents en choisissant les individus ayant la fitness la plus élevée, c'est-à-dire ceux ayant parcouru la plus courte distance. Cette approche vise à favoriser la reproduction des individus les plus performants, dans l'espoir de transmettre leurs caractéristiques bénéfiques à la génération suivante. En sélectionnant les parents de cette manière, j'espère améliorer progressivement la qualité des solutions au fil des générations.
     d. Création de nouveaux individus : (crossover + mutation) 
Croisement (Crossover) :
Choisissez deux parents parmi les individus sélectionnés à l'étape précédente.
Choisissez un point de croisement aléatoire sur les chemins des parents.
Échangez les parties des chemins des parents à partir du point de croisement pour créer les chemins des enfants.
Répétez ce processus jusqu'à obtenir le nombre d'enfants souhaité.
en respectant le fait de ne pas passer par une ville plusieurs fois 


Mutation :
Je parcoure chaque enfant généré après le croisement.
Pour chaque enfant, je selectionne de manière aléatoire si une mutation doit être appliquée. Vous pouvez utiliser le taux de mutation pour déterminer la probabilité de mutation.
Si une mutation est choisie, appliquez une opération de mutation. Par exemple, vous pouvez choisir deux positions aléatoires dans le chemin de l'enfant et échanger les villes à ces positions.

    e. Ajout des nouveaux individus dans la population : 
Vous avez intégré les nouveaux individus générés par croisement et mutation à la population existante.

        
