import numpy as np #librairi 
import matplotlib.pyplot as plt #pour les illustration graphiqie
import random as rd# pour generer aleatoirement les cordonnees des point des villes quand on descine les villes par des points ....
import tkinter as tk # pour créer votre interface graphique
from tkinter import simpledialog # pour utiliser simpledialog
from tkinter import messagebox


Pc=0.8 # taux de croisement
Pm=0.01 # taux de mutation
root = tk.Tk()
root.withdraw()  # Cacher la fenêtre principale
# Demander à l'utilisateur le nombre de villes à générer
#simpledialog.askinteger("Nombre de villes", "Entrez le nombre de villes à générer :")
while True:
        try:
            num_cities = int(simpledialog.askstring("Nombre de villes", "Entrez le nombre de villes à générer :"))
            if num_cities > 0:
                N= num_cities
                break
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier.")
# NOMBRE DE VILLES
 # DIMENSION DE LA POPULATION
while True:
        try:
            dimension_population = int(simpledialog.askstring("Dimension population", "Entrez la Dimension de la population :"))
            if dimension_population > 0:
                M= dimension_population
                break
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier.")
#k=0 #compteur pour la boucle apres
villes_dessinees = False  # Variable globale pour suivre si les villes ont été dessinées ou non





                    #     2      Evaluation de la "fitness" (qualité) des individus

# la fonction fitness : pour evaluer chaque chromosome(individue)
def fitness():# calcule la distance totale parcourue en suivant le chemin représenté par les indices de la variable chemin
    global chemin
    distance = 0.0
    xy=np.column_stack((x[chemin],y[chemin])) # Cette ligne crée un tableau bidimensionnel où chaque ligne représente les coordonnées (x, y) d'une ville dans l'ordre défini par le chemin actuel. La fonction np.column_stack() est utilisée pour empiler les tableaux x et y sur les colonnes, de sorte que chaque colonne contienne les coordonnées (x, y) d'une ville.
    distance=np.sum(np.sqrt(np.sum((xy- np.roll(xy,-1,axis=0))**2,axis=1))) # alcule la distance totale parcourue en suivant le chemin défini par les indices de la variable chemin. Elle utilise la fonction np.roll() pour décaler les éléments du tableau xy d'une position vers le haut, de sorte que la première ville visite la deuxième, la deuxième visite la troisième, et ainsi de suite. Ensuite, elle calcule la distance entre chaque paire de villes consécutives, puis somme ces distances pour obtenir la distance totale parcourue.
    return distance # la distance totale calculée comme mesure de fitness de l'individu.
"""J'ai défini une fonction pour calculer la distance entre deux villes. 
J'ai utilisé une formule de distance, telle que la distance euclidienne 
dans un espace bidimensionnel, car mes villes sont représentées par des coordonnées.
J'ai utilisé cette fonction pour calculer la distance totale parcourue par chaque individu dans la population.
J'ai noté que plus la distance est courte, meilleure est la fitness de l'individu. J'ai donc inversé la distance 
(par exemple, en prenant l'inverse de la distance) pour obtenir un score de fitness où une valeur plus élevée indique
 une meilleure adaptation.
J'ai attribué à chaque individu son score de fitness calculé.
J'ai répété ce processus pour tous les individus de la population.
"""


#+++++++
# les villes et leurs cordonnees , (chaque ville est représentée par ses coordonnées x et y dans un espace bidimensionnel)
x=np.random.uniform(0,1,N)#NumPy pour générer des coordonnées x et y aléatoires dans l'intervalle [0, 1] pour N villes
y=np.random.uniform(0,1,N)
chemin = np.arange(N)#crée un tableau NumPy contenant une séquence de nombres allant de 0 à N-1, représentant l'ordre initial dans lequel les villes sont visitées.



                  #         1     determiner la population initiale et le calcul de la fitness sur cette population

print('\n\n\n           MA POPULATION INITIAL ou chaque element et ca fitness calculer : \n\n\n  ')
population =[]  # une liste de listes représentant la population d'individus. Chaque individu est lui-même une liste représentant un chemin à travers les villes.la population c'est un ensmble de chromosome (on a 100) et chaque chromosome a 100 genes == on utilise une matrice
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
    print('chromosome numero ',i+1, population[i],'fitness = ', d)

# Calcul de fitness_population
print('\n\n\n           la FITNESS DE MA POPULATION INITIAL : \n\n\n  ')
fitness_population = []
for individu in population:
    chemin = individu
    d = fitness()
    fitness_population.append(d) #  je stocke ces résultats dans une liste appelée fitness_population
print(fitness_population) #test pour voir la fitness de la population


                            #               Trier les individus en fonction de leur fitness

#####(marche bien )la population trier selon la fitness
population_trier_fitness = list(zip(fitness_population, population))# Création d'une liste de tuples (fitness, individu)
population_trier_fitness.sort(key=lambda x: x[0])# Tri de la population en fonction de la fitness
fitness_population = list(fitness for fitness, _ in population_trier_fitness)# Séparation de la population triée et des fitness triées
population = list(individu for _, individu in population_trier_fitness)
print('\n\n\n           A CHAQUE FOIS JE TRIE MA FITNESSE POUR POUVOIR SELECTIONNER LES MEILLEUR INDIVIDUE POUR LE PROCHZINE CROISEMENT  : \n\n\n  ')
print(fitness_population) #test pour voir la fitness de la population





                            #     interface graphique


class TSPApp:      # j'ai difinis une classe appelée TSPApp pour mon application.
    def __init__(self, master):# Ceci est le constructeur de la classe TSPApp, il prend un argument master qui est la fenêtre principale de l'application.
        self.master = master
        master.title("Problème du Voyageur de Commerce")

        self.canvas = tk.Canvas(master, width=400, height=400) # zone de dessin) dans la fenêtre principale
        self.canvas.pack(fill=tk.BOTH, expand=True)  # affichons le canevas dans la fenêtre principale. canevas se redimensionne avec la fenêtre

        #self.run_button = tk.Button(master, text="Run Algorithme", command=self.run_algorithm)
        #self.run_button.pack(fill=tk.BOTH, expand=True)

        # Initialisation du texte affichant le numéro d'itération aligné à gauche
        self.iteration_text = self.canvas.create_text(10, 10, text="Iteration: 0", anchor="w")
        # Initialisation du texte affichant le meilleur individu aligné à droite à côté du premier texte
        #self.iteration_meilleur_individu = self.canvas.create_text(20, 20, text="meilleur individu : 0 ", anchor="e")
        
    def update_population_graph(self, population, index=0):
        global villes_dessinees
        if index < len(population):
            chemin = population[index]
            
            # Supprimer les chemins et les villes précédentes
            self.canvas.delete("chemins")
            #self.canvas.delete("villes")
            
            # Dessiner les nouvelles villes uniquement lors du premier appel
            if not villes_dessinees:
                #num_cities = self.get_num_cities_from_user()  # Obtenir le nombre de villes à générer de l'utilisateur
                for i in range(len(chemin)):
                    x_coord, y_coord = x[i]*400, y[i]*400
                    # Dessiner le cercle
                    rayon = 15
                    self.canvas.create_oval(x_coord-rayon, y_coord-rayon, x_coord+rayon, y_coord+rayon, fill="white", tags="villes")
                    # Afficher le numéro de la ville à l'intérieur du cercle
                    self.canvas.create_text(x_coord, y_coord, text=str(i), fill="black", tags="villes_text")
                villes_dessinees = True  # Mettre à jour la variable de suivi
                 

            # Dessiner le nouveau chemin pour l'individu actuel
            for i in range(len(chemin) - 1):
                ville1 = chemin[i]
                ville2 = chemin[i + 1]
                x1, y1 = x[ville1]*400, y[ville1]*400
                x2, y2 = x[ville2]*400, y[ville2]*400
                self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, tags="chemins")

            ville1 = chemin[-1]
            ville2 = chemin[0]
            x1, y1 = x[ville1]*400, y[ville1]*400
            x2, y2 = x[ville2]*400, y[ville2]*400
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, tags="chemins")

            # Appeler cette méthode avec un délai entre chaque appel
            self.master.after(200, self.update_population_graph, population, index + 1)
    
    #pour voir si l'algo a un certain moment cert plus et avance plus
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
    def selection_parents(self, population):
        # Définissez le nombre de parents à sélectionner
        taille_population = len(population)  # Taille de la population
        # Calcul du nombre de parents
        nombre_parents = int(taille_population * Pc)# taille_population*taux de croisement
        #indices_ordres = sorted(range(len(fitness_population)), key=lambda k: fitness_population[k])
        parents = population[:nombre_parents]
        #parents = [population[i] for i in indices_parents]
        return parents
    

                #       4         Création de nouveaux individus : crossover + mutation
    #pour verifier si l'individu a deja visite une ville 
    def verifier_redondance(self, chemin):
        villes_visitees = set()  # Utiliser un ensemble pour stocker les villes visitées
        chemin_sans_redondance = []  # Initialiser le chemin sans redondance

        for ville in chemin:
            if ville not in villes_visitees:
                chemin_sans_redondance.append(ville)
                villes_visitees.add(ville)
            else:
                # Trouver une ville non visitée
                nouvelle_ville = self.trouver_ville_non_visitee(villes_visitees)
                chemin_sans_redondance.append(nouvelle_ville)
                villes_visitees.add(nouvelle_ville)

        return chemin_sans_redondance

    def trouver_ville_non_visitee(self, villes_visitees):
        # Trouver une ville non visitée en vérifiant chaque ville possible
        for ville in range(N):
            if ville not in villes_visitees:
                return ville
        return -1  # Si toutes les villes sont visitées, retourner -1 ou une autre valeur indiquant l'erreur

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

                # Vérification des redondances pour l'enfant 1
                enfant1 = self.verifier_redondance(enfant1)
                # Vérification des redondances pour l'enfant 2
                enfant2 = self.verifier_redondance(enfant2)
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
    
    def affichage_results(self, best_individual,fitness, generation):
        # Créer une nouvelle fenêtre pour afficher les résultats
        root = tk.Tk()
        root.title("Résultats TSP")

        label = tk.Label(root, text=f"Meilleur individu trouvé à la génération {generation} trvaverse les villes avec cette ordre la : {best_individual}")
        label.pack()

        label = tk.Label(root, text=f"la fitness  : {fitness}")
        label.pack()

        button = tk.Button(root, text="Fermer", command=root.destroy)
        button.pack()

        root.mainloop()
# je ne l'ai pas utiliser plutardrrrrrr
    def element_deja_present(self, nouveaux_individus, population):
        """
        Vérifie si un élément est déjà présent dans la population.
        
        les Arguments:
            element: L'élément à vérifier.
            population: La population à parcourir.
            
        retour :
            True si l'élément est présent dans la population, False sinon.
        """
        elements_present = []
        for element in nouveaux_individus:
            element_present = any(individu == element for individu in population)
            elements_present.append(element_present)
        return elements_present


    def run_algorithm(self,population):
        global fitness_population
        # Initialiser les variables pour la boucle d'évolution
        num_iterations = 1000  # Nombre maximal d'itérations == generation 
        iteration = 0
        Seuil_Amelioration  = 1e-5  # Seuil d'amélioration de la fitness
         # Entrer dans la boucle d'évolution
        #self.update_population_graph(population)
        print('\n\n\n           Application de l ALGORITHME GENTIQUE  : \n\n\n  ')
        while iteration < num_iterations:
            
            # Sélectionner les parents en fonction de leur fitness
            parents_selectionnes = self.selection_parents(population)

            # Effectuer le croisement et la mutation pour créer de nouveaux individus
            nouveaux_individus = self.croisement_mutation(parents_selectionnes, Pc, Pm)
            print(nouveaux_individus)
#       5     Ajout des nouveaux individus dans la population :
            # Ajouter les nouveaux individus à la population
            nouveaux_individus_non_present = [individu for individu in nouveaux_individus 
                                          if not any(individu == element for element in population)]

            population.extend(nouveaux_individus_non_present)
            # Calculer la fitness de la nouvelle population
            fitness_nouvelle_population = [self.fitness(individu) for individu in population]

            # Vérifier si le critère d'arrêt est atteint
            #if self.check_convergence(fitness_population, fitness_nouvelle_population, Seuil_Amelioration):
                #break
            fitness_population = fitness_nouvelle_population

            #####(marche bien )la population trier selon la fitness
            population_trier_fitness = list(zip(fitness_population, population))# Création d'une liste de tuples (fitness, individu)
            population_trier_fitness.sort(key=lambda x: x[0])# Tri de la population en fonction de la fitness
            fitness_population = list(fitness for fitness, _ in population_trier_fitness)# Séparation de la population triée et des fitness triées
            population = list(individu for _, individu in population_trier_fitness)
            print(fitness_population) #test pour voir la fitness de la population

            # Mettre à jour la population et la fitness pour la prochaine itération
            population = population[:M]  # Garder seulement les M meilleurs individus
            iteration += 1

            # Mettre à jour l'affichage des résultats dans l'interface graphique (à implémenter)
            self.update_population_graph(population)

            # Mettre à jour le texte affichant le numéro d'itération
            self.canvas.itemconfig(self.iteration_text, text="Iteration: " + str(iteration))
            # Mettre à jour le texte affichant le meilleur individu
            #self.canvas.itemconfig(self.iteration_text, text="meilleur individu : " + str(fitness_population[0]))
            
            
            
            
            
            self.master.after(1000, self.run_algorithm, population, fitness_population, iteration + 1)  # 1000 millisecondes = 1 seconde

            #verification si vraiment les genration change
            print('\n\n      Generation ', iteration)
            for i in range(0,M,1) :
                print('chromosome mmmmm',i, population[i],'fitness = ', fitness_population[i])

            # Appeler la prochaine itération après un délai
            self.master.after(1000, self.run_algorithm, population, fitness_population, iteration + 1)  # 1000 millisecondes = 1 seconde
        #self.canvas.itemconfig(self.iteration_text, text="meilleur individu : " + str(fitness_population[0]))
        # Afficher les résultats finaux dans l'interface graphique (à implémenter)

        print('\n\n\n   Generation finale :  ', iteration)
        for i in range(0,M,1) :
            print('chromosome : ',i, population[i],'fitness = ', fitness_population[i])
        print('Meilleur individu(chromosome) trouvé : ',i, population[0],'ca est fitness = ', fitness_population[0],'\n\n\n\n\n\n')
        self.affichage_results(population[0],fitness_population[0], num_iterations )
        # À la fin de votre méthode run_algorithm, créez une nouvelle population contenant uniquement le meilleur individu pour l'afficher seul
        #best_individual = population[0]
        #best_population = [best_individual]    
        # Appelez la méthode update_population_graph avec cette population contenant uniquement le meilleur individu
        #self.update_population_graph(best_population)


root = tk.Tk()
app = TSPApp(root)
app.run_algorithm(population)
#app.update_population_graph(population)

root.mainloop()#pour démarrer la boucle principale de l'interface graphique.

            




            

