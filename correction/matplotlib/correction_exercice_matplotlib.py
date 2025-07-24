"""
CORRECTION - Exercice pratique: Visualisation de données avec Matplotlib et Pandas
=================================================================================

Solutions des exercices de visualisation de données
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
        """
        self.df = None
        self.load_data(file_path)
        
    def load_data(self, file_path):
        """
        SOLUTION Exercice 1 - Chargement et préparation des données
        """
        print("Chargement des données...")
        self.df = pd.read_csv(file_path)
        
        # Nettoyer les données de prix
        self.df["price"] = self.df.price.fillna(self.df.price.median())
        
        # Afficher les informations de base
        print(f"Données chargées: {self.df.shape[0]} lignes, {self.df.shape[1]} colonnes")
        print("\nPremières lignes:")
        print(self.df.head())
    
    def plot_points_distribution(self):
        """
        SOLUTION Exercice 2 - Histogramme de la distribution des points
        """
        plt.figure(figsize=(10, 6))
        plt.hist(self.df['points'], bins=20, color='blue', alpha=0.7)
        plt.title('Distribution des points des vins')
        plt.xlabel('Points')
        plt.ylabel('Nombre de vins')
        plt.grid(True, alpha=0.3)
        plt.savefig('histogramme_points.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_price_vs_points_scatter(self):
        """
        SOLUTION Exercice 3 - Diagramme de dispersion prix vs points
        """
        # Filtrer les données pour éviter les outliers
        filtered_data = self.df[self.df['price'] < 200]
        
        plt.figure(figsize=(10, 6))
        plt.scatter(filtered_data['points'], filtered_data['price'], 
                   color='green', s=5, alpha=0.6)
        plt.title('Relation entre Points et Prix des vins')
        plt.xlabel('Points')
        plt.ylabel('Prix ($)')
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def plot_top_countries_bar(self):
        """
        SOLUTION Exercice 4 - Graphique en barres des top 10 pays
        """
        top_countries = self.df['country'].value_counts().head(10)
        
        plt.figure(figsize=(12, 8))
        plt.barh(range(len(top_countries)), top_countries.values, color='red', alpha=0.7)
        plt.yticks(range(len(top_countries)), top_countries.index)
        plt.title('Top 10 des pays producteurs de vin')
        plt.xlabel('Nombre de vins')
        plt.ylabel('Pays')
        plt.gca().invert_yaxis()  # Pour avoir le plus grand en haut
        plt.tight_layout()
        plt.show()
    
    def plot_variety_pie_chart(self):
        """
        SOLUTION Exercice 5 - Diagramme circulaire des variétés de vin
        """
        top_varieties = self.df['variety'].value_counts().head(8)
        
        plt.figure(figsize=(10, 8))
        explode = [0.1, 0, 0, 0, 0, 0, 0, 0]  # Faire "exploser" la première tranche
        plt.pie(top_varieties.values, labels=top_varieties.index, autopct='%1.1f%%',
                explode=explode, startangle=90)
        plt.title('Répartition des 8 variétés de vin les plus communes')
        plt.axis('equal')  # Pour avoir un cercle parfait
        plt.show()
    
    def plot_multiple_subplots(self):
        """
        SOLUTION Exercice 6 - Graphiques multiples avec subplots
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # Subplot 1: Histogramme des points
        ax1.hist(self.df['points'], bins=20, color='blue', alpha=0.7)
        ax1.set_title('Distribution des points')
        ax1.set_xlabel('Points')
        ax1.set_ylabel('Fréquence')
        
        # Subplot 2: Scatter prix vs points (prix < 100)
        filtered_data = self.df[self.df['price'] < 100]
        ax2.scatter(filtered_data['points'], filtered_data['price'], alpha=0.6, s=3)
        ax2.set_title('Prix vs Points (< 100$)')
        ax2.set_xlabel('Points')
        ax2.set_ylabel('Prix ($)')
        
        # Subplot 3: Top 5 pays
        top_countries = self.df['country'].value_counts().head(5)
        ax3.bar(range(len(top_countries)), top_countries.values, color='green')
        ax3.set_title('Top 5 pays')
        ax3.set_xticks(range(len(top_countries)))
        ax3.set_xticklabels(top_countries.index, rotation=45)
        ax3.set_ylabel('Nombre de vins')
        
        # Subplot 4: Distribution des prix
        ax4.hist(self.df[self.df['price'] < 200]['price'], bins=30, color='orange', alpha=0.7)
        ax4.set_title('Distribution des prix (< 200$)')
        ax4.set_xlabel('Prix ($)')
        ax4.set_ylabel('Fréquence')
        
        plt.tight_layout()
        plt.savefig('analyse_complete.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_advanced_analysis(self):
        """
        SOLUTION Exercice 7 - Analyse avancée avec régression linéaire
        """
        # Filtrer les données
        filtered = self.df[
            (self.df['price'] >= 10) & 
            (self.df['price'] <= 100) & 
            (self.df['points'] >= 80) & 
            (self.df['points'] <= 100)
        ]
        
        plt.figure(figsize=(12, 8))
        
        # Scatter plot
        plt.scatter(filtered['points'], filtered['price'], alpha=0.6, color='blue', s=20)
        
        # Régression linéaire
        coeffs = np.polyfit(filtered['points'], filtered['price'], 1)
        line_x = np.linspace(filtered['points'].min(), filtered['points'].max(), 100)
        line_y = coeffs[0] * line_x + coeffs[1]
        
        plt.plot(line_x, line_y, color='red', linewidth=2, 
                label=f'y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}')
        
        plt.title(f'Régression linéaire: Prix vs Points\ny = {coeffs[0]:.2f}x + {coeffs[1]:.2f}')
        plt.xlabel('Points')
        plt.ylabel('Prix ($)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def plot_price_distribution_by_rating(self):
        """
        SOLUTION Exercice 8 - Analyse des prix par catégorie de notes
        """
        # Créer les catégories
        def categorize_rating(points):
            if points >= 95:
                return 'Excellent (≥95)'
            elif points >= 90:
                return 'Très bon (90-94)'
            elif points >= 85:
                return 'Bon (85-89)'
            else:
                return 'Moyen (<85)'
        
        self.df['rating_category'] = self.df['points'].apply(categorize_rating)
        
        # Filtrer les prix pour la lisibilité
        filtered_df = self.df[self.df['price'] < 200]
        
        # Préparer les données pour le box plot
        categories = ['Moyen (<85)', 'Bon (85-89)', 'Très bon (90-94)', 'Excellent (≥95)']
        price_data = [filtered_df[filtered_df['rating_category'] == cat]['price'].values 
                     for cat in categories]
        
        plt.figure(figsize=(12, 8))
        box_plot = plt.boxplot(price_data, labels=categories, patch_artist=True)
        
        # Colorier les boîtes
        colors = ['lightcoral', 'lightblue', 'lightgreen', 'gold']
        for patch, color in zip(box_plot['boxes'], colors):
            patch.set_facecolor(color)
        
        plt.title('Distribution des prix par catégorie de notes')
        plt.xlabel('Catégorie de notes')
        plt.ylabel('Prix ($)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()


# Exercices Bonus implémentés
class WineDataVisualizerBonus(WineDataVisualizer):
    """Extension avec les exercices bonus"""
    
    def plot_3d_analysis(self):
        """
        SOLUTION Exercice Bonus 1 - Graphique 3D
        """
        # Filtrer et échantillonner les données pour la performance
        sample_data = self.df.sample(n=1000, random_state=42)
        sample_data = sample_data.dropna(subset=['price', 'points'])
        
        fig = plt.figure(figsize=(12, 9))
        ax = fig.add_subplot(111, projection='3d')
        
        # Créer un index comme 3ème dimension
        z_values = range(len(sample_data))
        
        scatter = ax.scatter(sample_data['points'], sample_data['price'], z_values,
                           c=sample_data['points'], cmap='viridis', alpha=0.6)
        
        ax.set_xlabel('Points')
        ax.set_ylabel('Prix ($)')
        ax.set_zlabel('Index')
        ax.set_title('Analyse 3D: Points, Prix et Index')
        
        plt.colorbar(scatter)
        plt.show()
    
    def plot_correlation_heatmap(self):
        """
        SOLUTION Exercice Bonus 2 - Heatmap de corrélation
        """
        # Sélectionner les colonnes numériques
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        correlation_matrix = self.df[numeric_cols].corr()
        
        plt.figure(figsize=(10, 8))
        im = plt.imshow(correlation_matrix, cmap='coolwarm', aspect='auto')
        
        # Ajouter les labels
        plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
        plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
        
        # Ajouter les valeurs dans les cellules
        for i in range(len(correlation_matrix.columns)):
            for j in range(len(correlation_matrix.columns)):
                plt.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                        ha='center', va='center')
        
        plt.colorbar(im)
        plt.title('Matrice de corrélation des variables numériques')
        plt.tight_layout()
        plt.show()
    
    def demonstrate_styles(self):
        """
        SOLUTION Exercice Bonus 4 - Styles personnalisés
        """
        styles = ['default', 'ggplot', 'seaborn-v0_8', 'dark_background']
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        axes = axes.flatten()
        
        for i, style in enumerate(styles):
            plt.style.use(style)
            ax = axes[i]
            
            # Créer un graphique simple
            x = self.df['points'].sample(100)
            y = self.df['price'].sample(100)
            
            ax.scatter(x, y, alpha=0.6)
            ax.set_title(f'Style: {style}')
            ax.set_xlabel('Points')
            ax.set_ylabel('Prix')
        
        plt.tight_layout()
        plt.show()
        
        # Remettre le style par défaut
        plt.style.use('default')


def main():
    """
    Fonction principale pour exécuter tous les exercices et leurs corrections
    """
    file_path = r"..\..\data\pandas\winemag-data-130k-v2.csv"
    
    print("=== CORRECTIONS des exercices Matplotlib + Pandas ===")
    
    # Visualiseur principal
    visualizer = WineDataVisualizer(file_path)
    
    print("\n1. ✅ Données chargées et nettoyées")
    
    print("\n2. 📊 Histogramme des points...")
    visualizer.plot_points_distribution()
    
    print("\n3. 📈 Scatter plot prix vs points...")
    visualizer.plot_price_vs_points_scatter()
    
    print("\n4. 📊 Graphique en barres des pays...")
    visualizer.plot_top_countries_bar()
    
    print("\n5. 🥧 Diagramme circulaire des variétés...")
    visualizer.plot_variety_pie_chart()
    
    print("\n6. 📋 Analyse complète avec subplots...")
    visualizer.plot_multiple_subplots()
    
    print("\n7. 📉 Analyse avec régression linéaire...")
    visualizer.plot_advanced_analysis()
    
    print("\n8. 📦 Box plot par catégorie...")
    visualizer.plot_price_distribution_by_rating()
    
    # Exercices bonus
    print("\n=== EXERCICES BONUS ===")
    visualizer_bonus = WineDataVisualizerBonus(file_path)
    
    print("\n🎁 Bonus 1: Graphique 3D...")
    visualizer_bonus.plot_3d_analysis()
    
    print("\n🎁 Bonus 2: Heatmap de corrélation...")
    visualizer_bonus.plot_correlation_heatmap()
    
    print("\n🎁 Bonus 4: Démonstration des styles...")
    visualizer_bonus.demonstrate_styles()
    
    print("\n=== ✅ Tous les exercices sont terminés! ===")
    print("\nFichiers générés:")
    print("- histogramme_points.png")
    print("- analyse_complete.png")


if __name__ == "__main__":
    main()
