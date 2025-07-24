# Pandas Exercise - CORRECTION - Data Analysis with Wine Reviews
"""
CORRECTION - Exercice Pandas - Analyse de données avec les critiques de vins

Cette correction montre les solutions complètes pour tous les exercices pandas.
"""

import pandas as pd
import numpy as np

# Exercice 1 - Lecture et exploration des données
def load_and_explore_data(file_path):
    """
    Charge le dataset et retourne des informations de base.
    
    Args:
        file_path (str): Chemin vers le fichier CSV
        
    Returns:
        tuple: (DataFrame, nombre de lignes, nombre de colonnes, liste des colonnes)
    """
    # Charger le dataset avec la première colonne comme index
    df = pd.read_csv(file_path, index_col=0)
    
    # Retourner le DataFrame, le nombre de lignes, colonnes et la liste des noms de colonnes
    num_rows, num_cols = df.shape
    column_names = df.columns.tolist()
    
    return df, num_rows, num_cols, column_names


# Exercice 2 - Sélection et indexation
def analyze_country_data(df, country_name):
    """
    Analyse les données pour un pays spécifique.
    
    Args:
        df (DataFrame): Le dataset des vins
        country_name (str): Nom du pays à analyser
        
    Returns:
        tuple: (DataFrame filtré, nombre de vins, score moyen, prix moyen)
    """
    # Filtrer les données pour le pays spécifié
    country_data = df.loc[df['country'] == country_name]
    
    # Calculer le nombre de vins, score moyen et prix moyen
    wine_count = len(country_data)
    avg_score = country_data['points'].mean()
    avg_price = country_data['price'].mean()  # pandas ignore automatiquement les NaN
    
    return country_data, wine_count, avg_score, avg_price


# Exercice 3 - Sélection conditionnelle complexe
def find_premium_wines(df, min_score=90, max_price=50):
    """
    Trouve les vins avec un score élevé ET un prix raisonnable.
    
    Args:
        df (DataFrame): Le dataset des vins
        min_score (int): Score minimum requis
        max_price (float): Prix maximum accepté
        
    Returns:
        DataFrame: Vins répondant aux critères
    """
    # Sélectionner les vins avec score >= min_score ET prix <= max_price
    # Ne garder que les lignes où le prix n'est pas null
    premium_wines = df.loc[
        (df['points'] >= min_score) & 
        (df['price'] <= max_price) & 
        (df['price'].notnull())
    ]
    
    return premium_wines


# Exercice 4 - Fonctions de résumé et statistiques
def wine_statistics(df):
    """
    Calcule diverses statistiques sur le dataset.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        dict: Dictionnaire contenant les statistiques
    """
    stats = {}
    
    # Score moyen
    stats['avg_score'] = df['points'].mean()
    
    # Prix médian (ignorer les valeurs nulles)
    stats['median_price'] = df['price'].median()
    
    # Nombre de pays uniques
    stats['unique_countries'] = df['country'].nunique()
    
    # Top 5 des variétés les plus fréquentes (avec leur nombre)
    stats['top_varieties'] = df['variety'].value_counts().head().to_dict()
    
    # Dégustateur avec le plus de critiques
    stats['most_active_taster'] = df['taster_name'].value_counts().index[0]
    
    return stats


# Exercice 5 - Transformation avec map/apply
def create_price_categories(df):
    """
    Crée une nouvelle colonne catégorisant les vins par prix.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        DataFrame: Dataset avec la nouvelle colonne 'price_category'
    """
    # Créer une copie du DataFrame
    df_copy = df.copy()
    
    # Créer une fonction qui catégorise les prix
    def categorize_price(price):
        if pd.isnull(price):
            return 'Unknown'
        elif price <= 20:
            return 'Budget'
        elif price <= 50:
            return 'Mid-range'
        elif price <= 100:
            return 'Premium'
        else:
            return 'Luxury'
    
    # Appliquer la fonction à la colonne 'price' et créer 'price_category'
    df_copy['price_category'] = df_copy['price'].map(categorize_price)
    
    return df_copy


# Exercice 6 - Groupement et agrégation
def analyze_by_country_and_variety(df):
    """
    Analyse les données groupées par pays et variété.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        DataFrame: Analyse groupée avec statistiques
    """
    # Grouper par 'country' et 'variety'
    # Calculer pour chaque groupe: count, mean score, mean price, min price, max price
    grouped_analysis = df.groupby(['country', 'variety']).agg({
        'points': ['count', 'mean'],
        'price': ['mean', 'min', 'max']
    })
    
    # Aplatir les colonnes multi-niveaux
    grouped_analysis.columns = ['wine_count', 'avg_score', 'avg_price', 'min_price', 'max_price']
    
    # Réinitialiser l'index pour avoir un DataFrame plat
    grouped_analysis = grouped_analysis.reset_index()
    
    # Trier par nombre de vins (décroissant)
    grouped_analysis = grouped_analysis.sort_values('wine_count', ascending=False)
    
    return grouped_analysis


# Exercice 7 - Nettoyage des données manquantes
def clean_missing_data(df):
    """
    Nettoie les données manquantes selon des règles spécifiques.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        DataFrame: Dataset nettoyé
    """
    # Créer une copie du DataFrame
    df_clean = df.copy()
    
    # Pour la colonne 'price': remplacer les valeurs manquantes par la médiane
    median_price = df_clean['price'].median()
    df_clean['price'].fillna(median_price, inplace=True)
    
    # Pour la colonne 'region_2': remplacer les valeurs manquantes par 'Unknown'
    df_clean['region_2'].fillna('Unknown', inplace=True)
    
    # Pour la colonne 'taster_name': supprimer les lignes où cette valeur est manquante
    df_clean = df_clean.dropna(subset=['taster_name'])
    
    # Pour la colonne 'country': remplacer les valeurs manquantes par 'Unknown'
    df_clean['country'].fillna('Unknown', inplace=True)
    
    return df_clean


# Exercice 8 - Renommage et restructuration
def restructure_dataframe(df):
    """
    Renomme les colonnes et restructure le DataFrame.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        DataFrame: DataFrame restructuré
    """
    # Créer une copie du DataFrame
    df_restructured = df.copy()
    
    # Renommer les colonnes selon le mapping
    column_mapping = {
        'points': 'score',
        'taster_name': 'reviewer',
        'taster_twitter_handle': 'reviewer_twitter',
        'winery': 'producer'
    }
    df_restructured = df_restructured.rename(columns=column_mapping)
    
    # Renommer l'axe des lignes en 'wine_id' et l'axe des colonnes en 'attributes'
    df_restructured = df_restructured.rename_axis('wine_id', axis='rows')
    df_restructured = df_restructured.rename_axis('attributes', axis='columns')
    
    return df_restructured


# Exercice 9 - Analyse avancée avec conditions multiples
def advanced_wine_analysis(df):
    """
    Effectue une analyse avancée avec plusieurs conditions.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        dict: Résultats de l'analyse avancée
    """
    results = {}
    
    # Trouver le vin le plus cher et retourner son titre
    most_expensive_idx = df['price'].idxmax()
    results['most_expensive_wine'] = df.loc[most_expensive_idx, 'title']
    
    # Trouver le meilleur vin (score le plus haut) de moins de 30€
    budget_wines = df.loc[(df['price'] < 30) & (df['price'].notnull())]
    if not budget_wines.empty:
        best_budget_idx = budget_wines['points'].idxmax()
        results['best_budget_wine'] = budget_wines.loc[best_budget_idx, 'title']
    else:
        results['best_budget_wine'] = "Aucun vin trouvé"
    
    # Calculer le pourcentage de vins avec un score >= 95
    excellent_wines = df.loc[df['points'] >= 95]
    results['excellent_wine_percentage'] = (len(excellent_wines) / len(df)) * 100
    
    # Trouver les 3 pays avec le plus de variétés différentes
    country_varieties = df.groupby('country')['variety'].nunique().sort_values(ascending=False)
    results['most_diverse_countries'] = country_varieties.head(3).to_dict()
    
    # Calculer la corrélation entre le prix et le score (ignorer les valeurs nulles)
    clean_data = df[['price', 'points']].dropna()
    results['price_score_correlation'] = clean_data['price'].corr(clean_data['points'])
    
    return results


# Exercice 10 - Création d'un rapport de synthèse
def generate_wine_report(df):
    """
    Génère un rapport de synthèse complet du dataset.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        str: Rapport formaté en texte
    """
    report = "=== RAPPORT D'ANALYSE DES VINS ===\n\n"
    
    # Informations générales
    num_rows, num_cols = df.shape
    num_countries = df['country'].nunique()
    num_varieties = df['variety'].nunique()
    
    report += f"INFORMATIONS GÉNÉRALES:\n"
    report += f"- Nombre total de vins: {num_rows:,}\n"
    report += f"- Nombre de colonnes: {num_cols}\n"
    report += f"- Nombre de pays: {num_countries}\n"
    report += f"- Nombre de variétés: {num_varieties}\n\n"
    
    # Statistiques de base
    stats = wine_statistics(df)
    report += f"STATISTIQUES DE BASE:\n"
    report += f"- Score moyen: {stats['avg_score']:.2f}/100\n"
    report += f"- Prix médian: {stats['median_price']:.2f}€\n"
    report += f"- Dégustateur le plus actif: {stats['most_active_taster']}\n\n"
    
    # Top 5 des pays par nombre de vins
    top_countries = df['country'].value_counts().head()
    report += f"TOP 5 DES PAYS (par nombre de vins):\n"
    for i, (country, count) in enumerate(top_countries.items(), 1):
        report += f"{i}. {country}: {count:,} vins\n"
    report += "\n"
    
    # Top 5 des variétés
    report += f"TOP 5 DES VARIÉTÉS:\n"
    for i, (variety, count) in enumerate(stats['top_varieties'].items(), 1):
        report += f"{i}. {variety}: {count:,} vins\n"
    report += "\n"
    
    # Analyse des prix par catégorie
    df_with_categories = create_price_categories(df)
    price_analysis = df_with_categories['price_category'].value_counts()
    report += f"RÉPARTITION PAR CATÉGORIE DE PRIX:\n"
    for category, count in price_analysis.items():
        percentage = (count / len(df_with_categories)) * 100
        report += f"- {category}: {count:,} vins ({percentage:.1f}%)\n"
    
    # Analyse avancée
    advanced = advanced_wine_analysis(df)
    report += f"\nANALYSE AVANCÉE:\n"
    report += f"- Vin le plus cher: {advanced['most_expensive_wine']}\n"
    report += f"- Meilleur vin budget: {advanced['best_budget_wine']}\n"
    report += f"- Pourcentage de vins excellents (≥95): {advanced['excellent_wine_percentage']:.1f}%\n"
    report += f"- Corrélation prix/score: {advanced['price_score_correlation']:.3f}\n"
    
    return report


# Fonctions utilitaires supplémentaires pour les tests
def create_sample_dataset():
    """
    Crée un petit dataset d'exemple pour tester les fonctions.
    """
    data = {
        'country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Unknown'],
        'points': [95, 88, 92, 87, 90, 85],
        'price': [45.0, 25.0, None, 35.0, 55.0, 20.0],
        'variety': ['Chardonnay', 'Sangiovese', 'Tempranillo', 'Pinot Noir', 'Sangiovese', 'Merlot'],
        'taster_name': ['John', 'Maria', 'Pierre', 'John', None, 'Anna'],
        'title': ['Great French Wine', 'Nice Italian', 'Spanish Delight', 'Burgundy Special', 'Tuscan Beauty', 'Budget Choice'],
        'winery': ['Domaine A', 'Cantina B', 'Bodega C', 'Domaine D', 'Cantina E', 'Winery F'],
        'region_1': ['Burgundy', 'Tuscany', 'Rioja', 'Burgundy', 'Tuscany', None],
        'region_2': [None, None, 'Sub-region', None, None, None]
    }
    return pd.DataFrame(data)


if __name__ == "__main__":
    print("=== CORRECTION PANDAS EXERCISE ===\n")
    
    # Test avec un dataset d'exemple
    sample_df = create_sample_dataset()
    print("Dataset d'exemple créé:")
    print(sample_df)
    print(f"\nShape: {sample_df.shape}")
    
    # Test de quelques fonctions
    print("\n=== TESTS DES FONCTIONS ===")
    
    # Test statistiques
    stats = wine_statistics(sample_df)
    print(f"\nStatistiques:")
    for key, value in stats.items():
        print(f"- {key}: {value}")
    
    # Test catégorisation des prix
    df_with_categories = create_price_categories(sample_df)
    print(f"\nCatégories de prix:")
    print(df_with_categories[['price', 'price_category']])
    
    # Test nettoyage
    df_clean = clean_missing_data(sample_df)
    print(f"\nDataset nettoyé - Shape: {df_clean.shape}")
    print(f"Valeurs manquantes après nettoyage:")
    print(df_clean.isnull().sum())
    
    print("\n=== Tests terminés ===")
    print("Utilisez un vrai dataset de vins pour tester toutes les fonctionnalités!")
