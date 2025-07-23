# Pandas Exercise - Data Analysis with Wine Reviews
"""
Exercice Pandas - Analyse de données avec les critiques de vins

Dans cet exercice, vous allez travailler avec un dataset de critiques de vins.
Vous devez compléter les fonctions suivantes en utilisant les méthodes pandas appropriées.

Dataset: Un fichier CSV contenant des critiques de vins avec les colonnes:
- country: Pays d'origine du vin
- description: Description du vin
- designation: Désignation du vin
- points: Score attribué (80-100)
- price: Prix du vin
- province: Province/région
- region_1: Région principale
- region_2: Région secondaire
- taster_name: Nom du dégustateur
- taster_twitter_handle: Handle Twitter du dégustateur
- title: Titre de la critique
- variety: Variété du raisin
- winery: Nom de la cave
"""

import pandas as pd
import numpy as np

# TODO: Exercice 1 - Lecture et exploration des données
def load_and_explore_data(file_path=r"..\..\data\pandas\winemag-data-130k-v2.csv"):
    """
    Charge le dataset et retourne des informations de base.
    
    Args:
        file_path (str): Chemin vers le fichier CSV
        
    Returns:
        tuple: (DataFrame, nombre de lignes, nombre de colonnes, liste des colonnes)
    """
    # TODO: Charger le dataset avec la première colonne comme index
    df = pd.read_csv(file_path)
    df = df.set_index("Unnamed: 0").rename_axis("index", axis="rows")
    lignes = df.shape[0]
    columns = df.shape[1]
    liste = df.columns
    # TODO: Retourner le DataFrame, le nombre de lignes, colonnes et la liste des noms de colonnes
    return df, lignes, columns, liste


# TODO: Exercice 2 - Sélection et indexation
def analyze_country_data(df: pd.DataFrame, country_name: str):
    """
    Analyse les données pour un pays spécifique.
    
    Args:
        df (DataFrame): Le dataset des vins
        country_name (str): Nom du pays à analyser
        
    Returns:
        tuple: (DataFrame filtré, nombre de vins, score moyen, prix moyen)
    """
    # TODO: Filtrer les données pour le pays spécifié
    country_data = df.loc[df.country == country_name]
    
    
    # TODO: Calculer le nombre de vins, points moyen et prix moyen
    wine_count = country_data.shape[0]
    avg_score = country_data.points.mean()
    avg_price = country_data.price.mean()
    
    return country_data, wine_count, avg_score, avg_price


# TODO: Exercice 3 - Sélection conditionnelle complexe
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
    # TODO: Sélectionner les vins avec score >= min_score ET prix <= max_price
    # TODO: Ne garder que les lignes où le prix n'est pas null
    premium_wines = df.loc[(df.points >= min_score) & (df.price <= max_price)]
    
    return premium_wines


# TODO: Exercice 4 - Fonctions de résumé et statistiques
def wine_statistics(df: pd.DataFrame):
    """
    Calcule diverses statistiques sur le dataset.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        dict: Dictionnaire contenant les statistiques
    """
    stats = {}
    
    # TODO: Calculer les statistiques suivantes:
    # - Score moyen
    stats['avg_score'] = df.points.mean()
    
    # - Prix médian (ignorer les valeurs nulles)
    stats['median_price'] = df.points.median()
    
    # - Nombre de pays uniques
    stats['unique_countries'] = df.country.count()
    
    # - Top 5 des variétés les plus fréquentes (avec leur nombre)
    stats['top_varieties'] = df.variety.value_counts().head(5)
    
    # - Dégustateur avec le plus de critiques
    stats['most_active_taster'] = df.taster_name.value_counts().head(1)
    
    ## ATTENTION A SAVOIR QUOI RETOURNER (ex: stats['most_active_taster'] est une Series)
    return stats


# TODO: Exercice 5 - Transformation avec map/apply
def create_price_categories(df: pd.DataFrame):
    """
    Crée une nouvelle colonne catégorisant les vins par prix.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        DataFrame: Dataset avec la nouvelle colonne 'price_category'
    """
    # TODO: Créer une copie du DataFrame
    df_copy = df.copy(deep=True)
    
    # TODO: Créer une fonction qui catégorise les prix:
    # - 'Budget': prix <= 20
    # - 'Mid-range': 20 < prix <= 50
    # - 'Premium': 50 < prix <= 100
    # - 'Luxury': prix > 100
    # - 'Unknown': prix manquant
    def categorize_price(price):
        if price <= 20:
            return "Budget"
        elif price <= 50:
            return "Mid-range"
        elif price <= 100:
            return "Premium"
        elif price > 100:
            return "Luxury"
        else:
            return "Unknown"
    
    # TODO: Appliquer la fonction à la colonne 'price' et créer 'price_category'
    df_copy['price_category'] = df.price.map(categorize_price)

    return df_copy


# TODO: Exercice 6 - Groupement et agrégation
def analyze_by_country_and_variety(df: pd.DataFrame):
    """
    Analyse les données groupées par pays et variété.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        DataFrame: Analyse groupée avec statistiques
    """
    # TODO: Grouper par 'country' et 'variety'
    # TODO: Calculer pour chaque groupe: count, mean score, mean price, min price, max price
    grouped_analysis = df.groupby(["country", "variety"]).agg({
        'points': ['count', 'mean'],
        'price': ['mean', 'min', 'max']
    })
    
    # TODO: Réinitialiser l'index pour avoir un DataFrame plat
    # TODO: Trier par nombre de vins (décroissant)
    
    return grouped_analysis


# TODO: Exercice 7 - Nettoyage des données manquantes
def clean_missing_data(df: pd.DataFrame):
    """
    Nettoie les données manquantes selon des règles spécifiques.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        DataFrame: Dataset nettoyé
    """
    # TODO: Créer une copie du DataFrame
    df_clean = df.copy(deep=True)
    # reviews.region_2.fillna("Unknown")
    # TODO: Pour la colonne 'price': remplacer les valeurs manquantes par la médiane
    df_clean["price"] = df_clean.price.fillna(df_clean.price.median())
    
    # TODO: Pour la colonne 'region_2': remplacer les valeurs manquantes par 'Unknown'
    df_clean["region_2"] = df_clean.region_2.fillna("Unknown")

    # TODO: Pour la colonne 'taster_name': supprimer les lignes où cette valeur est manquante
    df_clean.dropna(subset=["taster_name"])

    # TODO: Pour la colonne 'country': remplacer les valeurs manquantes par 'Unknown'
    df_clean["country"] = df_clean.country.fillna("Unknown")
    
    return df_clean


# TODO: Exercice 8 - Renommage et restructuration
def restructure_dataframe(df: pd.DataFrame):
    """
    Renomme les colonnes et restructure le DataFrame.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        DataFrame: DataFrame restructuré
    """
    # TODO: Créer une copie du DataFrame
    df_restructured = df.copy(deep=True)
    
    # TODO: Renommer les colonnes selon ce mapping:
    column_mapping = {
        'points': 'score',
        'taster_name': 'reviewer',
        'taster_twitter_handle': 'reviewer_twitter',
        'winery': 'producer'
    }
    
    df_restructured = df_restructured.rename(column_mapping)
    
    # TODO: Renommer l'axe des lignes en 'wine_id' et l'axe des colonnes en 'attributes'
    df_restructured = df_restructured.rename_axis("wine_id").rename_axis("attributes", axis="columns")
    
    return df_restructured


# TODO: Exercice 9 - Analyse avancée avec conditions multiples
def advanced_wine_analysis(df):
    """
    Effectue une analyse avancée avec plusieurs conditions.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        dict: Résultats de l'analyse avancée
    """
    results = {}
    
    # TODO: Trouver le vin le plus cher et retourner son titre
    results['most_expensive_wine'] = df.loc[df.price.idxmax()][["price", "title"]]
    
    # TODO: Trouver le meilleur vin (score le plus haut) de moins de 30€
    max_score = df.loc[df.points.idxmax()]["points"]
    results['best_budget_wine'] = find_premium_wines(df, max_score, 30)
    
    # TODO: Calculer le pourcentage de vins avec un score >= 95
    results['excellent_wine_percentage'] = df.loc[df.points >= 95].shape[0] / df.shape[0] * 100
    
    # TODO: Trouver les 3 pays avec le plus de variétés différentes
    results['most_diverse_countries'] = None
    
    # TODO: Calculer la corrélation entre le prix et le score (ignorer les valeurs nulles)
    results['price_score_correlation'] = None
    
    return results


# TODO: Exercice 10 - Création d'un rapport de synthèse
def generate_wine_report(df):
    """
    Génère un rapport de synthèse complet du dataset.
    
    Args:
        df (DataFrame): Le dataset des vins
        
    Returns:
        str: Rapport formaté en texte
    """
    # TODO: Utiliser les fonctions précédentes pour créer un rapport complet
    # TODO: Le rapport doit inclure:
    # - Informations générales (nombre de vins, pays, etc.)
    # - Statistiques de base (scores, prix)
    # - Top 5 des pays par nombre de vins
    # - Top 5 des variétés
    # - Analyse des prix par catégorie
    
    report = "=== RAPPORT D'ANALYSE DES VINS ===\n\n"
    
    # TODO: Compléter le rapport avec toutes les informations demandées
    
    return report


# Fonction pour créer un dataset de test
def create_test_dataset():
    """
    Crée un dataset de test pour valider les fonctions.
    
    Returns:
        DataFrame: Dataset de test avec des données cohérentes
    """
    data = {
        'country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'US', 'Germany', 'Italy'],
        'description': ['A great wine', 'Nice Italian wine', 'Spanish red', 'Burgundy white', 'Tuscan red', 'California Cab', 'German Riesling', 'Chianti'],
        'designation': ['Special Reserve', 'Riserva', 'Gran Reserva', 'Premier Cru', 'Classico', 'Estate', 'Kabinett', 'DOCG'],
        'points': [95, 88, 92, 87, 90, 85, 89, 91],
        'price': [45.0, 25.0, None, 35.0, 55.0, 20.0, 28.0, 32.0],
        'province': ['Burgundy', 'Tuscany', 'Rioja', 'Burgundy', 'Tuscany', 'California', 'Mosel', 'Tuscany'],
        'region_1': ['Côte de Beaune', 'Chianti Classico', 'Rioja Alta', 'Chablis', 'Brunello', 'Napa Valley', 'Mosel-Saar-Ruwer', 'Chianti'],
        'region_2': [None, None, 'Sub-region', None, None, 'Oakville', None, None],
        'taster_name': ['John Smith', 'Maria Rossi', 'Pierre Dubois', 'John Smith', None, 'Anna Johnson', 'Klaus Weber', 'Maria Rossi'],
        'taster_twitter_handle': ['@johnsmith', '@mariarossi', '@pierredubois', '@johnsmith', None, '@anna_wine', '@klausweber', '@mariarossi'],
        'title': ['Great French Wine 2020', 'Nice Italian 2019', 'Spanish Delight 2018', 'Burgundy Special 2021', 'Tuscan Beauty 2019', 'Budget Choice 2020', 'German Precision 2020', 'Classic Chianti 2019'],
        'variety': ['Chardonnay', 'Sangiovese', 'Tempranillo', 'Chardonnay', 'Sangiovese', 'Cabernet Sauvignon', 'Riesling', 'Sangiovese'],
        'winery': ['Domaine Martin', 'Cantina Bella', 'Bodega Carlos', 'Domaine Dubois', 'Tenuta Grande', 'Valley Winery', 'Weingut Schmidt', 'Villa Toscana']
    }
    return pd.DataFrame(data)


# Tests d'assertion pour valider les fonctions
def run_assertion_tests():
    """
    Exécute des tests d'assertion pour valider toutes les fonctions de l'exercice.
    """
    print("=== DÉBUT DES TESTS D'ASSERTION ===\n")
    
    # Créer le dataset de test
    test_df = create_test_dataset()
    print(f"✅ Dataset de test créé: {test_df.shape[0]} lignes, {test_df.shape[1]} colonnes")
    
    # Test 1: load_and_explore_data
    print("\n📊 Test 1: load_and_explore_data")
    try:
        # Pour ce test, nous utilisons directement le DataFrame créé
        df, rows, cols, column_names = test_df, test_df.shape[0], test_df.shape[1], test_df.columns.tolist()
        
        # Assertions
        assert isinstance(df, pd.DataFrame), "Le retour doit être un DataFrame"
        assert rows == 8, f"Le nombre de lignes doit être 8, got {rows}"
        assert cols == 13, f"Le nombre de colonnes doit être 13, got {cols}"
        assert len(column_names) == 13, "La liste des colonnes doit contenir 13 éléments"
        assert 'country' in column_names, "La colonne 'country' doit être présente"
        assert 'points' in column_names, "La colonne 'points' doit être présente"
        print("✅ Test 1 réussi")
    except Exception as e:
        print(f"❌ Test 1 échoué: {e}")
    
    # Test 2: analyze_country_data
    print("\n🇫🇷 Test 2: analyze_country_data")
    try:
        country_data, wine_count, avg_score, avg_price = analyze_country_data(test_df, 'France')
        
        # Assertions
        assert isinstance(country_data, pd.DataFrame), "country_data doit être un DataFrame"
        assert wine_count == 2, f"La France doit avoir 2 vins, got {wine_count}"
        assert avg_score == 91.0, f"Score moyen pour la France doit être 91.0, got {avg_score}"
        assert avg_price == 40.0, f"Prix moyen pour la France doit être 40.0, got {avg_price}"
        print("✅ Test 2 réussi")
    except Exception as e:
        print(f"❌ Test 2 échoué: {e}")
    
    # Test 3: find_premium_wines
    print("\n💎 Test 3: find_premium_wines")
    try:
        premium_wines = find_premium_wines(test_df, min_score=90, max_price=50)
        
        # Assertions
        assert isinstance(premium_wines, pd.DataFrame), "premium_wines doit être un DataFrame"
        expected_wines = test_df[(test_df['points'] >= 90) & (test_df['price'] <= 50) & (test_df['price'].notnull())]
        assert len(premium_wines) == len(expected_wines), f"Nombre de vins premium incorrect"
        assert all(premium_wines['points'] >= 90), "Tous les vins doivent avoir un score >= 90"
        assert all(premium_wines['price'] <= 50), "Tous les vins doivent avoir un prix <= 50"
        print("✅ Test 3 réussi")
    except Exception as e:
        print(f"❌ Test 3 échoué: {e}")
    
    # Test 4: wine_statistics
    print("\n📈 Test 4: wine_statistics")
    try:
        stats = wine_statistics(test_df)
        
        # Assertions
        assert isinstance(stats, dict), "stats doit être un dictionnaire"
        assert 'avg_score' in stats, "avg_score doit être présent"
        assert 'median_price' in stats, "median_price doit être présent"
        assert 'unique_countries' in stats, "unique_countries doit être présent"
        assert 'top_varieties' in stats, "top_varieties doit être présent"
        assert 'most_active_taster' in stats, "most_active_taster doit être présent"
        
        assert abs(stats['avg_score'] - 89.625) < 0.01, f"Score moyen incorrect: {stats['avg_score']}"
        assert stats['unique_countries'] == 5, f"Nombre de pays uniques incorrect: {stats['unique_countries']}"
        print("✅ Test 4 réussi")
    except Exception as e:
        print(f"❌ Test 4 échoué: {e}")
    
    # Test 5: create_price_categories
    print("\n🏷️ Test 5: create_price_categories")
    try:
        df_with_categories = create_price_categories(test_df)
        
        # Assertions
        assert isinstance(df_with_categories, pd.DataFrame), "Résultat doit être un DataFrame"
        assert 'price_category' in df_with_categories.columns, "Colonne price_category doit être présente"
        assert len(df_with_categories) == len(test_df), "Le nombre de lignes doit être conservé"
        
        # Vérifier quelques catégories spécifiques
        budget_wines = df_with_categories[df_with_categories['price_category'] == 'Budget']
        assert len(budget_wines) > 0, "Il doit y avoir des vins Budget"
        unknown_wines = df_with_categories[df_with_categories['price_category'] == 'Unknown']
        assert len(unknown_wines) == 1, "Il doit y avoir 1 vin avec prix Unknown"
        print("✅ Test 5 réussi")
    except Exception as e:
        print(f"❌ Test 5 échoué: {e}")
    
    # Test 6: analyze_by_country_and_variety
    print("\n👥 Test 6: analyze_by_country_and_variety")
    try:
        grouped_analysis = analyze_by_country_and_variety(test_df)
        
        # Assertions
        assert isinstance(grouped_analysis, pd.DataFrame), "Résultat doit être un DataFrame"
        assert 'country' in grouped_analysis.columns, "Colonne country doit être présente"
        assert 'variety' in grouped_analysis.columns, "Colonne variety doit être présente"
        assert len(grouped_analysis) > 0, "Il doit y avoir des résultats groupés"
        print("✅ Test 6 réussi")
    except Exception as e:
        print(f"❌ Test 6 échoué: {e}")
    
    # Test 7: clean_missing_data
    print("\n🧹 Test 7: clean_missing_data")
    try:
        df_clean = clean_missing_data(test_df)
        
        # Assertions
        assert isinstance(df_clean, pd.DataFrame), "Résultat doit être un DataFrame"
        assert df_clean['price'].isnull().sum() == 0, "Aucune valeur manquante dans price après nettoyage"
        assert df_clean['region_2'].isnull().sum() == 0, "Aucune valeur manquante dans region_2 après nettoyage"
        assert df_clean['taster_name'].isnull().sum() == 0, "Aucune valeur manquante dans taster_name après nettoyage"
        assert df_clean['country'].isnull().sum() == 0, "Aucune valeur manquante dans country après nettoyage"
        print("✅ Test 7 réussi")
    except Exception as e:
        print(f"❌ Test 7 échoué: {e}")
    
    # Test 8: restructure_dataframe
    print("\n🔄 Test 8: restructure_dataframe")
    try:
        df_restructured = restructure_dataframe(test_df)
        
        # Assertions
        assert isinstance(df_restructured, pd.DataFrame), "Résultat doit être un DataFrame"
        assert 'score' in df_restructured.columns, "Colonne score doit être présente (renommée depuis points)"
        assert 'reviewer' in df_restructured.columns, "Colonne reviewer doit être présente"
        assert 'producer' in df_restructured.columns, "Colonne producer doit être présente"
        assert 'points' not in df_restructured.columns, "Colonne points ne doit plus être présente"
        print("✅ Test 8 réussi")
    except Exception as e:
        print(f"❌ Test 8 échoué: {e}")
    
    # Test 9: advanced_wine_analysis
    print("\n🔬 Test 9: advanced_wine_analysis")
    try:
        results = advanced_wine_analysis(test_df)
        
        # Assertions
        assert isinstance(results, dict), "Résultat doit être un dictionnaire"
        assert 'most_expensive_wine' in results, "most_expensive_wine doit être présent"
        assert 'best_budget_wine' in results, "best_budget_wine doit être présent"
        assert 'excellent_wine_percentage' in results, "excellent_wine_percentage doit être présent"
        assert 'most_diverse_countries' in results, "most_diverse_countries doit être présent"
        assert 'price_score_correlation' in results, "price_score_correlation doit être présent"
        
        assert isinstance(results['excellent_wine_percentage'], (int, float)), "excellent_wine_percentage doit être numérique"
        assert 0 <= results['excellent_wine_percentage'] <= 100, "Pourcentage doit être entre 0 et 100"
        print("✅ Test 9 réussi")
    except Exception as e:
        print(f"❌ Test 9 échoué: {e}")
    
    # Test 10: generate_wine_report
    print("\n📋 Test 10: generate_wine_report")
    try:
        report = generate_wine_report(test_df)
        
        # Assertions
        assert isinstance(report, str), "Le rapport doit être une chaîne de caractères"
        assert len(report) > 0, "Le rapport ne doit pas être vide"
        assert "RAPPORT D'ANALYSE DES VINS" in report, "Le titre doit être présent"
        print("✅ Test 10 réussi")
    except Exception as e:
        print(f"❌ Test 10 échoué: {e}")
    
    print("\n=== FIN DES TESTS D'ASSERTION ===")
    print("🎉 Tous les tests disponibles ont été exécutés!")
    print("\n💡 Note: Certains tests peuvent échouer si les fonctions ne sont pas encore implémentées.")
    print("Complétez les fonctions TODO pour que tous les tests passent.")


if __name__ == "__main__":
    print("=== EXERCICE PANDAS - TESTS D'ASSERTION ===\n")
    
    # Créer et afficher le dataset de test
    test_df = create_test_dataset()
    print("📊 Dataset de test créé:")
    print(test_df)
    print(f"\nShape: {test_df.shape}")
    print(f"Colonnes: {list(test_df.columns)}")
    
    # Informations sur les valeurs manquantes
    print(f"\n🔍 Valeurs manquantes par colonne:")
    missing_info = test_df.isnull().sum()
    for col, missing_count in missing_info.items():
        if missing_count > 0:
            print(f"- {col}: {missing_count} valeurs manquantes")
    
    print("\n" + "="*50)
    
    # Exécuter les tests d'assertion
    run_assertion_tests()
    
    print("\n" + "="*50)
    print("💻 Pour tester avec un vrai dataset CSV:")
    print("df, rows, cols, column_names = load_and_explore_data('path/to/winemag-data.csv')")
    print("print(f'Dataset chargé: {rows} lignes, {cols} colonnes')")
