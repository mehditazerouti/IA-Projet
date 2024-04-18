import numpy as np #librairi 
import matplotlib.pyplot as plt #pour les illustration graphiqie
import random as rd# pour generer aleatoirement les cordonnees des point des villes quand on descine les villes par des points ....
import tkinter as tk # pour créer votre interface graphique
from tkinter import simpledialog # pour utiliser simpledialog
from tkinter import messagebox

Pc=0.8 # taux de croisement
Pm=0.001 # taux de mutation
N=20# NOMBRE DE VILLES
M=100 # DIMENSION DE LA POPULATION
k=0 #compteur pour la boucle apres





                    #     2      Evaluation de la "fitness" (qualité) des individus

# la fonction fitness : pour evaluer chaque chromosome(individue)
def fitness():# calcule la distance totale parcourue en suivant le chemin représenté par les indices de la variable chemin
    global chemin
    distance = 0.0
    xy=np.column_stack((x[chemin],y[chemin])) # Cette ligne crée un tableau bidimensionnel où chaque ligne représente les coordonnées (x, y) d'une ville dans l'ordre défini par le chemin actuel. La fonction np.column_stack() est utilisée pour empiler les tableaux x et y sur les colonnes, de sorte que chaque colonne contienne les coordonnées (x, y) d'une ville.
    distance=np.sum(np.sqrt(np.sum((xy- np.roll(xy,-1,axis=0))**2,axis=1))) # alcule la distance totale parcourue en suivant le chemin défini par les indices de la variable chemin. Elle utilise la fonction np.roll() pour décaler les éléments du tableau xy d'une position vers le haut, de sorte que la première ville visite la deuxième, la deuxième visite la troisième, et ainsi de suite. Ensuite, elle calcule la distance entre chaque paire de villes consécutives, puis somme ces distances pour obtenir la distance totale parcourue.
    return distance # la distance totale calculée comme mesure de fitness de l'individu.



#+++++++
# les villes et leurs cordonnees , (chaque ville est représentée par ses coordonnées x et y dans un espace bidimensionnel)
x=np.random.uniform(0,1,N)#NumPy pour générer des coordonnées x et y aléatoires dans l'intervalle [0, 1] pour N villes
y=np.random.uniform(0,1,N)
chemin = np.arange(N)#crée un tableau NumPy contenant une séquence de nombres allant de 0 à N-1, représentant l'ordre initial dans lequel les villes sont visitées.



                  #         1     determiner la population initiale et le calcul de la fitness sur cette population


population =[]  # la population c'est un ensmble de chromosome (on a 100) et chaque chromosome a 100 genes == on utilise une matrice
for i in range(0,M,1) : # iterer avec i de 0 a M en avancant de 1
    #iniialiser la matrice : 
    population.append([0]*N)#append ajoute un element a la matrice
    for j in range(0,N,1) :
        villeVisiter=1   #booleen je l'utilise pour ne pas avoir de redendance de ville dans le meme parcours(qui est une contrainte de porbleme de voyageur)  pour controler le choix du numero
        if j == 0 : 
            element=rd.randint(0,N-1)# (rd=random) ranint donne un entier random car les element de la population c'est des int
        else : 
            while villeVisiter==1 :# tant que =1 repeter le randint
                element =rd.randint(0,N-1)
                cmpt=0 #un petit compteur pour compter le nombre de redendance de chque numero deja rempli 
                for k in range(0,j,1):# pour verifier les element deja remplie de 0 a J car on remplie jusqua maintenat jusqua j 
                    if population[i][k]==element :# si il y'a un element deja chosi egale au nombre random donner alors : 
                        villeVisiter=1
                        cmpt=cmpt+1
                if cmpt==0: villeVisiter=0

        population[i][j]=element
        chemin[j]= population[i][j]
        d=fitness()
    print('chromosome mmmmm',i, population[i],'fitness = ', d)

# Calcul de fitness_population
fitness_population = []
for individu in population:
    chemin = individu
    d = fitness()
    fitness_population.append(d) #  je stocke ces résultats dans une liste appelée fitness_population
#print(fitness_population) #test pour voir la fitness de la population


                            #               Trier les individus en fonction de leur fitness

population_triee = [x for _, x in sorted(zip(fitness_population, population))]
#####(marche bien )print('orde fitnesse : ',population_triee) #test pour voir la population trier selon la fitness



                            #     interface graphique


class TSPApp:      # j'ai difinis une classe appelée TSPApp pour mon application.
    def __init__(self, master):# Ceci est le constructeur de la classe TSPApp, il prend un argument master qui est la fenêtre principale de l'application.
        self.master = master
        master.title("Problème du Voyageur de Commerce")

        self.canvas = tk.Canvas(master, width=400, height=400) # zone de dessin) dans la fenêtre principale 
        self.canvas.pack() # affichons le canevas dans la fenêtre principale.

        self.generate_button = tk.Button(master, text="Générer Villes", command=self.generate_cities)
        self.generate_button.pack()

    def generate_cities(self):# bouton "Générer Villes" est cliqué
        self.canvas.delete("all")  # Effacer toutes les anciennes villes

        #num_cities = 10  # Nombre de villes à générer
        num_cities = self.get_num_cities_from_user()  # Obtenir le nombre de villes à générer de l'utilisateur
        for _ in range(num_cities):
            x = rd.randint(50, 350)  # Coordonnée x aléatoire dans la plage de 50 à 350 pixels.
            y = rd.randint(50, 350)  # Coordonnée y aléatoire
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")  # Dessiner la ville comme un cercle rouge avec un rayon 3

    def get_num_cities_from_user(self): # demander a l'utilisateur de donner le nombre de villes a generer 
        num_cities = simpledialog.askinteger("Nombre de villes", "Entrez le nombre de villes à générer :", initialvalue=10)
        return num_cities if num_cities else 10  # Retourne le nombre de villes saisi par l'utilisateur, ou 10 par défaut

    def update_graph(self, chemin):
            # Effacer les chemins précédents
        self.canvas.delete("chemins")

        # Dessiner les chemins pour chaque individu de la population
        for individu in population:
            chemin = individu
            if chemin:
                for i in range(len(chemin) - 1):
                    ville1 = chemin[i]
                    ville2 = chemin[i + 1]
                    x1, y1 = x[ville1], y[ville1]
                    x2, y2 = x[ville2], y[ville2]
                    self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, tags="chemins")

                # Dessiner le chemin de retour à la première ville
                ville1 = chemin[-1]
                ville2 = chemin[0]
                x1, y1 = x[ville1], y[ville1]
                x2, y2 = x[ville2], y[ville2]
                self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, tags="chemins")


    def check_convergence(self, fitness_population, fitness_nouvelle_population, Seuil_Amelioration):
        # Calculer la différence entre les fitness de la population actuelle et de la nouvelle population
        difference_fitness = abs(sum(fitness_population) - sum(fitness_nouvelle_population))

        # Vérifier si la différence est inférieure au seuil d'amélioration
        if difference_fitness < Seuil_Amelioration:
            return True  # Convergence atteinte
        else:
            return False  # Continuer l'algorithme


                     #    3    Sélection des parents

    def fitness(self, individu):# calcule la distance totale parcourue en suivant le chemin représenté par les indices de la variable chemin
        chemin=individu
        distance = 0.0
        xy=np.column_stack((x[chemin],y[chemin])) # Cette ligne crée un tableau bidimensionnel où chaque ligne représente les coordonnées (x, y) d'une ville dans l'ordre défini par le chemin actuel. La fonction np.column_stack() est utilisée pour empiler les tableaux x et y sur les colonnes, de sorte que chaque colonne contienne les coordonnées (x, y) d'une ville.
        distance=np.sum(np.sqrt(np.sum((xy- np.roll(xy,-1,axis=0))**2,axis=1))) # alcule la distance totale parcourue en suivant le chemin défini par les indices de la variable chemin. Elle utilise la fonction np.roll() pour décaler les éléments du tableau xy d'une position vers le haut, de sorte que la première ville visite la deuxième, la deuxième visite la troisième, et ainsi de suite. Ensuite, elle calcule la distance entre chaque paire de villes consécutives, puis somme ces distances pour obtenir la distance totale parcourue.
        return distance # la distance totale calculée comme mesure de fitness de l'individu.

    # Fonction de sélection des parents basée sur la fitness
    def selection_parents(self, population, fitness_population):
        # Définissez le nombre de parents à sélectionner
        taille_population = len(population)  # Taille de la population
        # Calcul du nombre de parents
        nombre_parents = int(taille_population * Pc )# taille_population*taux de croisement
        indices_ordres = sorted(range(len(fitness_population)), key=lambda k: fitness_population[k])
        indices_parents = indices_ordres[:nombre_parents]
        parents = [population[i] for i in indices_parents]
        return parents
    

                #       4         Création de nouveaux individus : crossover + mutation

    # Fonction de croisement (crossover) et mutation
    def croisement_mutation(self, parents_selectionnes, Pc, Pm):
        nouveaux_individus = []   # stocker les nouveaux individus créés.
        for i in range(len(parents_selectionnes) // 2):  # À chaque itération, deux parents sont extraits (parent1 et parent2) pour le croisement.
            parent1 = parents_selectionnes[2 * i]
            parent2 = parents_selectionnes[2 * i + 1]
            
            # Croisement (crossover) # On décide si le croisement se produit en fonction du taux de croisement    
            # on tire au hazard avec random un nombre de 0 a 1 et on le compare a Pc 
            if np.random.rand() < Pc:# nombres aléatoires  dans l'intervalle [0, 1)  On décide si le croisement se produit en fonction du taux de croisement Pc
                point_de_croisement = rd.randint(1, len(parent1) - 1)#  Choix aléatoire d'un point de croisement
                # Création des enfants en croisant les chemins des parents
                enfant1 = parent1[:point_de_croisement] + parent2[point_de_croisement:]
                enfant2 = parent2[:point_de_croisement] + parent1[point_de_croisement:]

                    # Mutation
                # Mutation de l'enfant 1  # chaque enfant subit une mutation avec une probabilité Pm Pour chaque enfant, deux positions sont choisies aléatoirement et les villes correspondantes sont échangées
                if np.random.rand() < Pm: # nombres aléatoires  dans l'intervalle [0, 1)         
                    positions = rd.sample(range(len(enfant1)), 2) # Choix aléatoire de deux positions à échanger
                    enfant1[positions[0]], enfant1[positions[1]] = enfant1[positions[1]], enfant1[positions[0]] # l'echange
                
                # Mutation de l'enfant 2
                if np.random.rand() < Pm:   # nombres aléatoires  dans l'intervalle [0, 1)
                    positions = rd.sample(range(len(enfant2)), 2)                # Choix aléatoire de deux positions à échanger
                    enfant2[positions[0]], enfant2[positions[1]] = enfant2[positions[1]], enfant2[positions[0]]# l'echange
                
                # Ajout des enfants à la liste des nouveaux individus
                nouveaux_individus.append(enfant1)
                nouveaux_individus.append(enfant2)
        
        return nouveaux_individus
    
    def run_algorithm(self,population, fitness_population):
        # Initialiser la population et calculer la fitness initiale
        population_init = population
        fitness_population_init = fitness_population

        # Initialiser les variables pour la boucle d'évolution
        num_iterations = 100  # Nombre maximal d'itérations
        iteration = 0
        Seuil_Amelioration  = 1e-5  # Seuil d'amélioration de la fitness
         # Entrer dans la boucle d'évolution
        while iteration < num_iterations:
            # Sélectionner les parents en fonction de leur fitness
            parents_selectionnes = self.selection_parents(population_init, fitness_population_init)

            # Effectuer le croisement et la mutation pour créer de nouveaux individus
            nouveaux_individus = self.croisement_mutation(parents_selectionnes, Pc, Pm)

#       5     Ajout des nouveaux individus dans la population :


            # Ajouter les nouveaux individus à la population
            population_init.extend(nouveaux_individus)

            # Calculer la fitness de la nouvelle population
            fitness_nouvelle_population = [self.fitness(individu) for individu in population_init]
            fitness_population_init=fitness_nouvelle_population

            # modifier la liste des chemin pour les dessiner 
            #chemins_population = []
            #for individu in population:
            #    chemins_population.append(np.copy(chemin))
                
            # Mettre à jour l'affichage des résultats dans l'interface graphique (à implémenter)
            self.update_graph(population_init)

    
            # Vérifier si le critère d'arrêt est atteint
            if self.check_convergence(fitness_population, fitness_nouvelle_population, Seuil_Amelioration):
                break

            # Mettre à jour la population et la fitness pour la prochaine itération
            population = population[:M]  # Garder seulement les M meilleurs individus
            fitness_population = fitness_nouvelle_population
            iteration += 1

        # Afficher les résultats finaux dans l'interface graphique (à implémenter)

root = tk.Tk()
app = TSPApp(root)
app.run_algorithm(population, fitness_population)
root.mainloop()

            










#GRAPHIQUE
plt.plot(x[chemin],y[chemin],marker='o', color='b')# la fonction plot() de matplotlib pour tracer le chemin représenté par les coordonnées des villes dans l'ordre défini par la variable chemin. Cependant, vous rencontrez une erreur à cet endroit.
