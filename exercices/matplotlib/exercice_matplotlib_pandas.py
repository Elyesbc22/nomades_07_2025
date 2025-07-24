"""
Exercice pratique: Visualisation de données avec Matplotlib et Pandas
==================================================================

Cet exercice utilise le dataset des vins pour créer différents types de graphiques
en utilisant les concepts vus dans le cours matplotlib.

Dataset: winemag-data-130k-v2.csv
Objectif: Créer des visualisations pour analyser les données des vins
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuration pour l'affichage des graphiques
plt.style.use('default')

class WineDataVisualizer:
    """Classe pour visualiser les données des vins avec matplotlib"""
    
    def __init__(self, file_path):
        """
        Initialise le visualiseur avec les données des vins
        
        Args:
            file_path (str): Chemin vers le fichier CSV des vins
        """
        self.df = None
        self.fp = file_path
        self.load_data(file_path)
        
    def load_data(self, file_path):
        """
        TODO: Exercice 1 - Chargement et préparation des données
        
        Instructions:
        1. Charger les données avec pandas
        2. Nettoyer les données de prix (remplacer les NaN par la médiane)
        3. Afficher les 5 premières lignes
        """
        # TODO: Compléter cette méthode
        df = pd.read_csv(file_path)
        df = df.fillna(df.mean())
        print(df.head(5))
        self.df = df
        
    def plot_points_distribution(self):
        """
        TODO: Exercice 2 - Histogramme de la distribution des points
        
        Instructions:
        1. Créer un histogramme des points (colonne 'points')
        2. Utiliser 20 bins
        3. Couleur: bleu avec transparence (alpha=0.7)
        4. Ajouter titre, labels des axes
        5. Sauvegarder le graphique sous 'histogramme_points.png'
        """
        # TODO: Compléter cette méthode
        
    
    def plot_price_vs_points_scatter(self):
        """
        TODO: Exercice 3 - Diagramme de dispersion prix vs points
        
        Instructions:
        1. Créer un scatter plot avec points en x et price en y
        2. Limiter aux vins avec prix < 200 (pour éviter les outliers)
        3. Utiliser des points verts de taille 5
        4. Ajouter une transparence (alpha=0.6)
        5. Ajouter titre et labels
        6. Afficher le graphique
        """
        # TODO: Compléter cette méthode
        pass
    
    def plot_top_countries_bar(self):
        """
        TODO: Exercice 4 - Graphique en barres des top 10 pays
        
        Instructions:
        1. Calculer le nombre de vins par pays (colonne 'country')
        2. Prendre les 10 premiers pays
        3. Créer un graphique en barres horizontal (barh)
        4. Couleur: rouge
        5. Ajouter titre et labels
        6. Faire une rotation des labels x si nécessaire
        """
        # TODO: Compléter cette méthode
        pass
    
    def plot_variety_pie_chart(self):
        """
        TODO: Exercice 5 - Diagramme circulaire des variétés de vin
        
        Instructions:
        1. Prendre les 8 variétés les plus communes (colonne 'variety')
        2. Créer un diagramme circulaire
        3. Afficher les pourcentages avec autopct='%1.1f%%'
        4. Faire "exploser" la première tranche (explode=[0.1, 0, 0, 0, 0, 0, 0, 0])
        5. Ajouter un titre
        """
        # TODO: Compléter cette méthode
        pass
    
    def plot_multiple_subplots(self):
        """
        TODO: Exercice 6 - Graphiques multiples avec subplots
        
        Instructions:
        1. Créer une figure avec 2x2 subplots
        2. Subplot 1 (1,1): Histogramme des points
        3. Subplot 2 (1,2): Scatter plot prix vs points (prix < 100)
        4. Subplot 3 (2,1): Barres des top 5 pays
        5. Subplot 4 (2,2): Distribution des prix (histogramme)
        6. Ajuster l'espacement avec plt.tight_layout()
        7. Sauvegarder sous 'analyse_complete.png'
        """
        # TODO: Compléter cette méthode
        pass
    
    def plot_advanced_analysis(self):
        """
        TODO: Exercice 7 - Analyse avancée avec régression linéaire
        
        Instructions:
        1. Filtrer les données: prix entre 10 et 100, points entre 80 et 100
        2. Créer un scatter plot prix vs points
        3. Calculer et tracer la ligne de régression linéaire (np.polyfit)
        4. Utiliser des couleurs différentes pour les points et la ligne
        5. Ajouter l'équation de la droite dans le titre
        6. Ajouter une grille (plt.grid(True))
        """
        # TODO: Compléter cette méthode
        pass
    
    def plot_price_distribution_by_rating(self):
        """
        TODO: Exercice 8 - Analyse des prix par catégorie de notes
        
        Instructions:
        1. Créer des catégories de notes:
           - Excellent: points >= 95
           - Très bon: 90 <= points < 95
           - Bon: 85 <= points < 90
           - Moyen: points < 85
        2. Créer un box plot des prix pour chaque catégorie
        3. Limiter les prix à < 200 pour la lisibilité
        4. Ajouter titre et labels
        """
        # TODO: Compléter cette méthode
        pass


def main():
    """
    Fonction principale pour exécuter tous les exercices
    """
    # Chemin vers le fichier de données
    file_path = r"..\..\data\pandas\winemag-data-130k-v2.csv"
    
    # Initialiser le visualiseur
    visualizer = WineDataVisualizer(file_path)
    
    print("=== Exercices de visualisation avec Matplotlib ===")
    
    # Exercice 1: Chargement des données
    print("\n1. Chargement et exploration des données...")
    # La méthode load_data est appelée automatiquement
    
    # Exercice 2: Histogramme
    print("\n2. Création de l'histogramme des points...")
    visualizer.plot_points_distribution()
    
    # Exercice 3: Scatter plot
    print("\n3. Création du scatter plot prix vs points...")
    visualizer.plot_price_vs_points_scatter()
    
    # Exercice 4: Graphique en barres
    print("\n4. Création du graphique en barres des pays...")
    visualizer.plot_top_countries_bar()
    
    # Exercice 5: Diagramme circulaire
    print("\n5. Création du diagramme circulaire des variétés...")
    visualizer.plot_variety_pie_chart()
    
    # Exercice 6: Subplots multiples
    print("\n6. Création des graphiques multiples...")
    visualizer.plot_multiple_subplots()
    
    # Exercice 7: Analyse avec régression
    print("\n7. Analyse avancée avec régression linéaire...")
    visualizer.plot_advanced_analysis()
    
    # Exercice 8: Box plot
    print("\n8. Analyse des prix par catégorie...")
    visualizer.plot_price_distribution_by_rating()
    
    print("\n=== Tous les exercices sont terminés! ===")


if __name__ == "__main__":
    main()


"""
BONUS: Exercices supplémentaires à implémenter

TODO: Exercice Bonus 1 - Graphique 3D
Créer un graphique 3D avec:
- X: points
- Y: prix
- Z: année (si disponible) ou utiliser un index
Utiliser plt.subplot(projection='3d')

TODO: Exercice Bonus 2 - Heatmap avec matplotlib
Créer une heatmap showing la corrélation entre:
- Points, prix, et d'autres variables numériques
Utiliser plt.imshow() avec une colormap

TODO: Exercice Bonus 3 - Animation
Créer une animation montrant l'évolution des données dans le temps
Utiliser matplotlib.animation si les données temporelles sont disponibles

TODO: Exercice Bonus 4 - Styles personnalisés
Expérimenter avec différents styles:
- plt.style.use('ggplot')
- plt.style.use('seaborn')
- plt.style.use('dark_background')

TODO: Exercice Bonus 5 - Graphiques interactifs
Ajouter des éléments interactifs comme:
- Zoom
- Tooltips
- Sélection de données
"""
