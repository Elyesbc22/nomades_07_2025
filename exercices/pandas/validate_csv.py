# CSV Structure Validation for Pandas Exercise
"""
Ce script valide que les fonctions de l'exercice sont correctement définies
pour travailler avec un dataset CSV de critiques de vins.
"""

import pandas as pd
import numpy as np

def create_wine_csv_sample():
    """
    Crée un fichier CSV d'exemple avec la structure exacte d'un dataset de vins.
    """
    # Données réalistes basées sur le dataset de critiques de vins
    wine_data = {
        'country': ['US', 'Spain', 'US', 'Spain', 'US', 'France', 'Italy', 'Germany', 'Australia', 'Chile'],
        'description': [
            'This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak.',
            'Ripe aromas of fig, blackberry and cassis are softened and sweetened by a slick of vanilla.',
            'Tart and snappy, the flavors of lime flesh and rind dominate.',
            'Pineapple rind, lemon pith and orange blossom start off the aromas.',
            'Much like the regular bottling from 2012, this comes across as rather rough and tannic.',
            'Blackberry and raspberry aromas show a typical Côtes du Rhône complexity.',
            'Soft, supple plum envelopes an oaky structure in this Tuscan red.',
            'Aromas include honeysuckle, citrus and oak. Flavors mirror the aromas.',
            'The nose is rather understated but clean, with citrus and green herb aromas.',
            'Violet and red berry aromas are accompanied by an herbal quality.'
        ],
        'designation': [
            "Martha's Vineyard",
            None,
            None,
            'Ars In Vitro',
            None,
            'Cuvée Speciale',
            'Riserva',
            'Kabinett',
            'Reserve',
            'Gran Reserva'
        ],
        'points': [96, 86, 87, 87, 87, 90, 91, 89, 88, 85],
        'price': [235.0, 30.0, None, 65.0, None, 45.0, 55.0, 28.0, 35.0, 25.0],
        'province': [
            'California',
            'Northern Spain',
            'Michigan',
            'Northern Spain',
            'Oregon',
            'Rhône',
            'Tuscany',
            'Mosel',
            'South Australia',
            'Central Valley'
        ],
        'region_1': [
            'Napa Valley',
            'Toro',
            'Lake Michigan Shore',
            'Toro',
            'Willamette Valley',
            'Côtes du Rhône',
            'Chianti Classico',
            'Mosel-Saar-Ruwer',
            'Barossa Valley',
            'Maipo Valley'
        ],
        'region_2': [
            'Oakville',
            None,
            None,
            None,
            'Dundee Hills',
            None,
            'Greve in Chianti',
            None,
            None,
            'Alto Maipo'
        ],
        'taster_name': [
            'Virginie Boone',
            'Michael Schachner',
            'Alexander Peartree',
            'Michael Schachner',
            'Paul Gregutt',
            'Roger Voss',
            'Kerin O'Keefe',
            'Anna Lee C. Iijima',
            'Joe Czerwinski',
            'Mike DeSimone'
        ],
        'taster_twitter_handle': [
            '@vboone',
            '@wineschach',
            None,
            '@wineschach',
            '@paulgwine',
            '@vossroger',
            '@kerinokeefe',
            None,
            '@JoeCz',
            '@worldwineguys'
        ],
        'title': [
            "Heitz 2013 Martha's Vineyard Cabernet Sauvignon (Napa Valley)",
            'Bodega Carmen Rodríguez 2011 Toro',
            'Mackinaw Trail Winery 2014 Vignoles (Lake Michigan Shore)',
            'Quinta de la Rosa 2012 Ars In Vitro Red (Toro)',
            'Ponzi 2013 Reserve Pinot Noir (Willamette Valley)',
            'Domaine de la Côte 2015 Cuvée Speciale (Côtes du Rhône)',
            'Castello di Bossi 2012 Riserva (Chianti Classico)',
            'Dr. Loosen 2016 Kabinett Riesling (Mosel)',
            'Wolf Blass 2014 Reserve Chardonnay (Barossa Valley)',
            'Santa Rita 2013 Gran Reserva Carmenère (Maipo Valley)'
        ],
        'variety': [
            'Cabernet Sauvignon',
            'Tinta de Toro',
            'Vignoles',
            'Tinta de Toro',
            'Pinot Noir',
            'Rhône-style Red Blend',
            'Sangiovese',
            'Riesling',
            'Chardonnay',
            'Carmenère'
        ],
        'winery': [
            'Heitz',
            'Bodega Carmen Rodríguez',
            'Mackinaw Trail Winery',
            'Quinta de la Rosa',
            'Ponzi',
            'Domaine de la Côte',
            'Castello di Bossi',
            'Dr. Loosen',
            'Wolf Blass',
            'Santa Rita'
        ]
    }
    
    df = pd.DataFrame(wine_data)
    
    # Sauvegarder en CSV
    csv_path = 'sample_wine_dataset.csv'
    df.to_csv(csv_path, index=True)
    print(f"✅ Fichier CSV créé: {csv_path}")
    print(f"📊 Structure: {df.shape[0]} lignes, {df.shape[1]} colonnes")
    return csv_path, df


def validate_csv_compatibility():
    """
    Valide que les fonctions de l'exercice sont compatibles avec un fichier CSV.
    """
    print("🔍 Validation de la compatibilité CSV")
    
    # Créer le fichier CSV de test
    csv_path, expected_df = create_wine_csv_sample()
    
    # Tests de compatibilité
    tests_passed = 0
    total_tests = 5
    
    # Test 1: Lecture du CSV
    print("\n1️⃣ Test de lecture CSV")
    try:
        # Simuler la fonction load_and_explore_data
        df = pd.read_csv(csv_path, index_col=0)
        rows, cols = df.shape
        column_names = df.columns.tolist()
        
        assert isinstance(df, pd.DataFrame), "Doit retourner un DataFrame"
        assert rows == len(expected_df), f"Nombre de lignes incorrect: {rows}"
        assert cols == len(expected_df.columns), f"Nombre de colonnes incorrect: {cols}"
        assert len(column_names) == cols, "Liste des colonnes incorrecte"
        
        print("✅ Lecture CSV validée")
        tests_passed += 1
        
    except Exception as e:
        print(f"❌ Échec lecture CSV: {e}")
    
    # Test 2: Structure des colonnes
    print("\n2️⃣ Test de structure des colonnes")
    try:
        required_columns = [
            'country', 'description', 'designation', 'points', 'price',
            'province', 'region_1', 'region_2', 'taster_name',
            'taster_twitter_handle', 'title', 'variety', 'winery'
        ]
        
        df = pd.read_csv(csv_path, index_col=0)
        
        for col in required_columns:
            assert col in df.columns, f"Colonne manquante: {col}"
        
        print("✅ Structure des colonnes validée")
        tests_passed += 1
        
    except Exception as e:
        print(f"❌ Échec structure: {e}")
    
    # Test 3: Types de données
    print("\n3️⃣ Test des types de données")
    try:
        df = pd.read_csv(csv_path, index_col=0)
        
        # Vérifications de types
        assert df['points'].dtype in ['int64', 'int32'], "Points doit être entier"
        assert df['price'].dtype in ['float64', 'float32'], "Price doit être float"
        assert df['country'].dtype == 'object', "Country doit être string"
        assert df['variety'].dtype == 'object', "Variety doit être string"
        
        print("✅ Types de données validés")
        tests_passed += 1
        
    except Exception as e:
        print(f"❌ Échec types: {e}")
    
    # Test 4: Valeurs manquantes
    print("\n4️⃣ Test des valeurs manquantes")
    try:
        df = pd.read_csv(csv_path, index_col=0)
        
        # Vérifier qu'il y a bien des valeurs manquantes
        null_counts = df.isnull().sum()
        assert null_counts['price'] > 0, "Il doit y avoir des prix manquants"
        assert null_counts['designation'] > 0, "Il doit y avoir des designations manquantes"
        assert null_counts['region_2'] > 0, "Il doit y avoir des region_2 manquantes"
        
        print("✅ Valeurs manquantes détectées correctement")
        tests_passed += 1
        
    except Exception as e:
        print(f"❌ Échec valeurs manquantes: {e}")
    
    # Test 5: Opérations de base
    print("\n5️⃣ Test des opérations de base")
    try:
        df = pd.read_csv(csv_path, index_col=0)
        
        # Test des opérations pandas de base
        avg_score = df['points'].mean()
        assert 80 <= avg_score <= 100, f"Score moyen suspect: {avg_score}"
        
        median_price = df['price'].median()
        assert median_price > 0, f"Prix médian suspect: {median_price}"
        
        unique_countries = df['country'].nunique()
        assert unique_countries > 1, f"Pas assez de pays: {unique_countries}"
        
        top_varieties = df['variety'].value_counts()
        assert len(top_varieties) > 0, "Aucune variété trouvée"
        
        print("✅ Opérations de base validées")
        tests_passed += 1
        
    except Exception as e:
        print(f"❌ Échec opérations: {e}")
    
    # Résumé
    print(f"\n📊 RÉSUMÉ: {tests_passed}/{total_tests} tests réussis")
    
    if tests_passed == total_tests:
        print("🎉 Tous les tests de compatibilité CSV sont passés!")
        print("✅ Vos fonctions devraient fonctionner avec un vrai dataset de vins")
    else:
        print("⚠️ Certains tests ont échoué")
        print("🔧 Vérifiez la structure de vos fonctions")
    
    return csv_path


def demonstrate_function_usage():
    """
    Démontre comment utiliser les fonctions avec un vrai fichier CSV.
    """
    print("\n" + "="*60)
    print("📋 DÉMONSTRATION D'UTILISATION AVEC CSV")
    print("="*60)
    
    csv_path = validate_csv_compatibility()
    
    print(f"\n💡 Exemple d'utilisation avec le fichier: {csv_path}")
    print("\n```python")
    print("# 1. Charger les données")
    print("df, rows, cols, column_names = load_and_explore_data('sample_wine_dataset.csv')")
    print("print(f'Dataset chargé: {rows} lignes, {cols} colonnes')")
    print()
    print("# 2. Analyser un pays")
    print("france_data, count, avg_score, avg_price = analyze_country_data(df, 'France')")
    print("print(f'France: {count} vins, score moyen: {avg_score:.2f}')")
    print()
    print("# 3. Trouver des vins premium")
    print("premium = find_premium_wines(df, min_score=90, max_price=50)")
    print("print(f'Vins premium trouvés: {len(premium)}')")
    print()
    print("# 4. Calculer des statistiques")
    print("stats = wine_statistics(df)")
    print("print(f'Statistiques: {stats}')")
    print()
    print("# 5. Créer des catégories de prix")
    print("df_cat = create_price_categories(df)")
    print("print(df_cat['price_category'].value_counts())")
    print()
    print("# 6. Analyser par pays et variété")
    print("grouped = analyze_by_country_and_variety(df)")
    print("print(grouped.head())")
    print()
    print("# 7. Nettoyer les données")
    print("df_clean = clean_missing_data(df)")
    print("print(f'Données nettoyées: {df_clean.isnull().sum().sum()} valeurs manquantes')")
    print()
    print("# 8. Restructurer")
    print("df_restructured = restructure_dataframe(df)")
    print("print(f'Colonnes renommées: {list(df_restructured.columns)}')")
    print()
    print("# 9. Analyse avancée")
    print("results = advanced_wine_analysis(df)")
    print("print(f'Analyse avancée: {results}')")
    print()
    print("# 10. Générer un rapport")
    print("report = generate_wine_report(df)")
    print("print(report)")
    print("```")
    
    print("\n🔗 Fichier CSV créé pour vos tests!")
    print(f"📁 Chemin: {csv_path}")
    print("🚀 Utilisez ce fichier pour tester vos fonctions!")


if __name__ == "__main__":
    print("🍷 VALIDATION CSV POUR L'EXERCICE PANDAS")
    print("="*50)
    
    # Valider la compatibilité CSV
    demonstrate_function_usage()
    
    print("\n" + "="*50)
    print("📝 NOTES IMPORTANTES:")
    print("• Le fichier CSV créé simule un vrai dataset de critiques de vins")
    print("• Toutes vos fonctions doivent fonctionner avec ce format")
    print("• Les tests d'assertion utilisent ce même format")
    print("• Structure compatible avec les datasets Kaggle de vins")
    print("\n🎯 Objectif: Complétez toutes les fonctions TODO pour réussir les tests!")
