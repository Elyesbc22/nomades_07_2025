# Test file for Pandas Exercise
"""
Tests d'assertion pour l'exercice Pandas - Analyse de données avec les critiques de vins

Ce fichier contient des tests complets pour valider toutes les fonctions de l'exercice.
Exécutez ce fichier pour vérifier que vos implémentations sont correctes.
"""

import pandas as pd
import numpy as np
import sys
import os

# Ajouter le répertoire parent au path pour importer ex.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Essayer d'importer les fonctions de l'exercice
try:
    from ex import *
    print("✅ Import des fonctions de l'exercice réussi")
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    print("Assurez-vous que le fichier ex.py est dans le même répertoire")
    sys.exit(1)


def create_comprehensive_test_dataset():
    """
    Crée un dataset de test plus complet pour des tests robustes.
    """
    np.random.seed(42)  # Pour des résultats reproductibles
    
    countries = ['France', 'Italy', 'Spain', 'US', 'Germany', 'Australia', 'Chile', 'Argentina']
    varieties = ['Chardonnay', 'Sangiovese', 'Tempranillo', 'Cabernet Sauvignon', 'Riesling', 'Pinot Noir', 'Merlot', 'Sauvignon Blanc']
    tasters = ['John Smith', 'Maria Rossi', 'Pierre Dubois', 'Anna Johnson', 'Klaus Weber', 'Sofia Garcia']
    
    # Créer 50 vins pour des tests plus robustes
    data = {
        'country': np.random.choice(countries, 50),
        'description': [f'Description du vin {i}' for i in range(50)],
        'designation': [f'Designation {i}' for i in range(50)],
        'points': np.random.randint(80, 101, 50),  # Scores entre 80 et 100
        'price': np.concatenate([
            np.random.uniform(15, 80, 45),  # 45 vins avec prix
            [None] * 5  # 5 vins sans prix
        ]),
        'province': [f'Province {i}' for i in range(50)],
        'region_1': [f'Region {i}' for i in range(50)],
        'region_2': np.concatenate([
            [f'Sub-region {i}' for i in range(30)],  # 30 avec region_2
            [None] * 20  # 20 sans region_2
        ]),
        'taster_name': np.concatenate([
            np.random.choice(tasters, 45),  # 45 avec dégustateur
            [None] * 5  # 5 sans dégustateur
        ]),
        'taster_twitter_handle': [f'@taster{i}' if i < 45 else None for i in range(50)],
        'title': [f'Wine Title {i}' for i in range(50)],
        'variety': np.random.choice(varieties, 50),
        'winery': [f'Winery {i}' for i in range(50)]
    }
    
    # Mélanger les données
    df = pd.DataFrame(data)
    return df.sample(frac=1).reset_index(drop=True)


def test_with_real_csv_structure():
    """
    Teste avec une structure similaire au vrai dataset CSV de vins.
    """
    print("\n🍷 Test avec structure CSV réaliste")
    
    # Données plus réalistes
    real_data = {
        'country': ['US', 'Spain', 'US', 'Spain', 'US', 'Spain', 'US', 'Spain'],
        'description': [
            'This tremendous 100% varietal wine hails from Oakville',
            'Ripe aromas of fig, blackberry and cassis',
            'Tart and snappy, the flavors of lime flesh and rind',
            'Pineapple rind, lemon pith and orange blossom',
            'Much like the regular bottling from 2012',
            'Blackberry and raspberry aromas show',
            'Soft, supple plum envelopes an oaky structure',
            'Balanced acidity and tannins frame'
        ],
        'designation': ['Martha\'s Vineyard', None, None, 'Ars In Vitro', None, None, 'Richard\'s Reserve', None],
        'points': [96, 86, 87, 87, 87, 87, 87, 87],
        'price': [235.0, 30.0, None, 65.0, None, 15.0, 60.0, None],
        'province': ['California', 'Northern Spain', 'Michigan', 'Northern Spain', 'Oregon', 'Northern Spain', 'Michigan', 'Northern Spain'],
        'region_1': ['Napa Valley', 'Toro', 'Lake Michigan Shore', 'Toro', 'Willamette Valley', 'Toro', 'Lake Michigan Shore', 'Toro'],
        'region_2': ['Oakville', None, None, None, 'Dundee Hills', None, None, None],
        'taster_name': ['Virginie Boone', 'Michael Schachner', 'Alexander Peartree', 'Michael Schachner', 'Paul Gregutt', 'Michael Schachner', 'Alexander Peartree', 'Michael Schachner'],
        'taster_twitter_handle': ['@vboone', '@wineschach', None, '@wineschach', '@paulgwine ', '@wineschach', None, '@wineschach'],
        'title': ['Heitz 2013 Martha\'s Vineyard Cabernet Sauvignon (Napa Valley)', 'Bodega Carmen Rodríguez 2011 Traverse Creek Red (Toro)', 'Mackinaw Trail Winery 2014 Vignoles (Lake Michigan Shore)', 'Quinta de la Rosa 2012 Ars In Vitro Red (Toro)', 'Ponzi 2013 Reserve Pinot Noir (Willamette Valley)', 'Quinta de la Rosa 2011 Red (Toro)', 'Mackinaw Trail Winery 2014 Richard\'s Reserve Red (Lake Michigan Shore)', 'Quinta de la Rosa 2010 Red (Toro)'],
        'variety': ['Cabernet Sauvignon', 'Tinta de Toro', 'Vignoles', 'Tinta de Toro', 'Pinot Noir', 'Tinta de Toro', 'Blend', 'Tinta de Toro'],
        'winery': ['Heitz', 'Bodega Carmen Rodríguez', 'Mackinaw Trail Winery', 'Quinta de la Rosa', 'Ponzi', 'Quinta de la Rosa', 'Mackinaw Trail Winery', 'Quinta de la Rosa']
    }
    
    real_df = pd.DataFrame(real_data)
    print(f"Dataset réaliste créé: {real_df.shape}")
    
    # Tests spécifiques avec données réalistes
    try:
        # Test des statistiques avec des données réelles
        stats = wine_statistics(real_df)
        print(f"✅ Statistiques calculées: score moyen = {stats['avg_score']:.2f}")
        
        # Test de filtrage par pays
        us_data, count, avg_score, avg_price = analyze_country_data(real_df, 'US')
        print(f"✅ Données US: {count} vins, score moyen = {avg_score:.2f}")
        
        # Test de catégorisation des prix
        df_cat = create_price_categories(real_df)
        categories = df_cat['price_category'].value_counts()
        print(f"✅ Catégories de prix: {dict(categories)}")
        
    except Exception as e:
        print(f"❌ Test avec données réalistes échoué: {e}")
    
    return real_df


def advanced_assertion_tests():
    """
    Tests d'assertion avancés avec validation de types et valeurs.
    """
    print("\n🔬 Tests d'assertion avancés")
    
    test_df = create_comprehensive_test_dataset()
    
    # Test avancé 1: Validation des types de retour
    print("\n1️⃣ Validation des types de retour")
    try:
        # Test load_and_explore_data (simulé)
        df, rows, cols, col_names = test_df, len(test_df), len(test_df.columns), list(test_df.columns)
        assert isinstance(df, pd.DataFrame), "DataFrame attendu"
        assert isinstance(rows, int), "Nombre de lignes doit être un entier"
        assert isinstance(cols, int), "Nombre de colonnes doit être un entier"
        assert isinstance(col_names, list), "Noms de colonnes doivent être une liste"
        print("✅ Types de retour validés")
        
    except Exception as e:
        print(f"❌ Validation des types échouée: {e}")
    
    # Test avancé 2: Cohérence des données après transformation
    print("\n2️⃣ Cohérence des données après transformation")
    try:
        original_shape = test_df.shape
        df_transformed = create_price_categories(test_df)
        
        assert df_transformed.shape[0] == original_shape[0], "Nombre de lignes doit être conservé"
        assert df_transformed.shape[1] == original_shape[1] + 1, "Une colonne doit être ajoutée"
        assert not df_transformed.equals(test_df), "Le DataFrame doit être modifié"
        print("✅ Cohérence des transformations validée")
        
    except Exception as e:
        print(f"❌ Validation de cohérence échouée: {e}")
    
    # Test avancé 3: Gestion des valeurs manquantes
    print("\n3️⃣ Gestion des valeurs manquantes")
    try:
        original_nulls = test_df.isnull().sum().sum()
        df_clean = clean_missing_data(test_df)
        final_nulls = df_clean.isnull().sum().sum()
        
        assert final_nulls < original_nulls, "Le nettoyage doit réduire les valeurs manquantes"
        assert df_clean['price'].isnull().sum() == 0, "Prix ne doit plus avoir de valeurs manquantes"
        print(f"✅ Valeurs manquantes réduites de {original_nulls} à {final_nulls}")
        
    except Exception as e:
        print(f"❌ Validation du nettoyage échouée: {e}")
    
    # Test avancé 4: Validation des calculs statistiques
    print("\n4️⃣ Validation des calculs statistiques")
    try:
        stats = wine_statistics(test_df)
        
        # Vérifications manuelles
        manual_avg = test_df['points'].mean()
        manual_median = test_df['price'].median()
        manual_countries = test_df['country'].nunique()
        
        assert abs(stats['avg_score'] - manual_avg) < 0.01, "Score moyen incorrect"
        assert abs(stats['median_price'] - manual_median) < 0.01, "Prix médian incorrect"
        assert stats['unique_countries'] == manual_countries, "Nombre de pays incorrect"
        print("✅ Calculs statistiques validés")
        
    except Exception as e:
        print(f"❌ Validation des statistiques échouée: {e}")
    
    # Test avancé 5: Performance et mémoire
    print("\n5️⃣ Tests de performance")
    try:
        import time
        
        # Test de performance sur groupement
        start_time = time.time()
        grouped = analyze_by_country_and_variety(test_df)
        end_time = time.time()
        
        assert end_time - start_time < 1.0, "Groupement trop lent"
        assert len(grouped) > 0, "Groupement doit retourner des résultats"
        print(f"✅ Groupement exécuté en {end_time - start_time:.3f}s")
        
    except Exception as e:
        print(f"❌ Test de performance échoué: {e}")


def edge_cases_tests():
    """
    Tests des cas limites et situations particulières.
    """
    print("\n🚨 Tests des cas limites")
    
    # Dataset vide
    print("\n📋 Test avec DataFrame vide")
    try:
        empty_df = pd.DataFrame(columns=['country', 'points', 'price', 'variety', 'taster_name'])
        stats = wine_statistics(empty_df)
        print("✅ Gestion du DataFrame vide validée")
    except Exception as e:
        print(f"⚠️ DataFrame vide non géré: {e}")
    
    # Dataset avec une seule ligne
    print("\n1️⃣ Test avec une seule ligne")
    try:
        single_df = pd.DataFrame({
            'country': ['France'],
            'points': [95],
            'price': [50.0],
            'variety': ['Chardonnay'],
            'taster_name': ['John'],
            'region_2': [None],
            'winery': ['Test Winery'],
            'title': ['Test Wine'],
            'taster_twitter_handle': ['@john']
        })
        
        stats = wine_statistics(single_df)
        assert stats['avg_score'] == 95, "Score unique doit être préservé"
        print("✅ Gestion d'une seule ligne validée")
    except Exception as e:
        print(f"⚠️ Une seule ligne non gérée: {e}")
    
    # Dataset avec toutes les valeurs manquantes dans une colonne
    print("\n❓ Test avec colonne entièrement manquante")
    try:
        all_null_df = create_comprehensive_test_dataset()
        all_null_df['price'] = None
        
        cleaned = clean_missing_data(all_null_df)
        print("✅ Gestion des colonnes entièrement nulles validée")
    except Exception as e:
        print(f"⚠️ Colonnes entièrement nulles non gérées: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("🧪 TESTS COMPLETS POUR L'EXERCICE PANDAS")
    print("=" * 60)
    
    # Tests de base
    print("\n📊 Création du dataset de test...")
    test_df = create_comprehensive_test_dataset()
    print(f"Dataset créé: {test_df.shape[0]} lignes, {test_df.shape[1]} colonnes")
    
    # Exécuter tous les tests
    try:
        print("\n🔧 Exécution des tests d'assertion de base...")
        run_assertion_tests()
        
        print("\n🍷 Tests avec structure CSV réaliste...")
        real_df = test_with_real_csv_structure()
        
        print("\n🔬 Tests d'assertion avancés...")
        advanced_assertion_tests()
        
        print("\n🚨 Tests des cas limites...")
        edge_cases_tests()
        
    except NameError as e:
        print(f"\n❌ Erreur: {e}")
        print("Certaines fonctions ne sont pas encore implémentées.")
        print("Complétez les fonctions dans ex.py pour exécuter tous les tests.")
    
    print("\n" + "=" * 60)
    print("🎯 RÉSUMÉ DES TESTS")
    print("=" * 60)
    print("✅ Tests basiques: Validation des fonctionnalités de base")
    print("🍷 Tests réalistes: Validation avec données similaires au vrai dataset")
    print("🔬 Tests avancés: Validation de la robustesse et performance")
    print("🚨 Tests limites: Validation des cas particuliers")
    print("\n💡 Assurez-vous que toutes les fonctions TODO sont implémentées!")
    print("🚀 Une fois tous les tests passés, votre exercice est terminé!")
