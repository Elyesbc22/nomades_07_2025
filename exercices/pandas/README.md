# Exercice Pandas - Analyse de données avec des critiques de vins

## Description

Cet exercice vous permettra de pratiquer les concepts fondamentaux de pandas en travaillant avec un dataset réaliste de critiques de vins. Vous allez apprendre à manipuler, analyser et transformer des données comme dans un projet d'analyse de données réel.

## Objectifs pédagogiques

À la fin de cet exercice, vous maîtriserez :
- 📊 **Lecture et exploration** de datasets avec pandas
- 🔍 **Sélection et indexation** (loc, iloc, conditions)
- 📈 **Fonctions de résumé** (describe, mean, median, value_counts)
- 🔄 **Transformations** avec map() et apply()
- 👥 **Groupement et agrégation** avec groupby()
- 🧹 **Nettoyage des données** manquantes
- 🏗️ **Restructuration** et renommage
- 📋 **Analyse avancée** avec conditions multiples

## Structure du projet

```
exercices/pandas/
├── ex.py              # Fichier d'exercice (à compléter)
└── README.md          # Ce fichier

correction/pandas/
└── ex.py              # Correction complète
```

## Dataset utilisé

L'exercice est conçu pour fonctionner avec un dataset de critiques de vins contenant les colonnes suivantes :

| Colonne | Description |
|---------|-------------|
| `country` | Pays d'origine du vin |
| `description` | Description détaillée du vin |
| `designation` | Désignation spécifique du vin |
| `points` | Score attribué (échelle 80-100) |
| `price` | Prix du vin en euros |
| `province` | Province/région d'origine |
| `region_1` | Région principale |
| `region_2` | Région secondaire (optionnel) |
| `taster_name` | Nom du dégustateur |
| `taster_twitter_handle` | Handle Twitter du dégustateur |
| `title` | Titre de la critique |
| `variety` | Variété du raisin |
| `winery` | Nom de la cave/producteur |

## Instructions

### Étape 1 : Préparation
1. Ouvrez le fichier `ex.py`
2. Assurez-vous d'avoir pandas et numpy installés
3. Téléchargez un dataset de critiques de vins (ou utilisez le dataset d'exemple dans la correction)

### Étape 2 : Complétion des exercices
Complétez les 10 fonctions dans l'ordre :

1. **`load_and_explore_data()`** - Chargement et exploration de base
2. **`analyze_country_data()`** - Analyse par pays
3. **`find_premium_wines()`** - Sélection conditionnelle
4. **`wine_statistics()`** - Calcul de statistiques
5. **`create_price_categories()`** - Transformation des données
6. **`analyze_by_country_and_variety()`** - Groupement et agrégation
7. **`clean_missing_data()`** - Nettoyage des valeurs manquantes
8. **`restructure_dataframe()`** - Renommage et restructuration
9. **`advanced_wine_analysis()`** - Analyse avancée
10. **`generate_wine_report()`** - Création d'un rapport complet

### Étape 3 : Test
Testez vos fonctions avec un dataset réel ou le dataset d'exemple fourni dans la correction.

## Concepts pandas couverts

### Lecture et exploration
- `pd.read_csv()` avec différents paramètres
- `shape`, `columns`, `head()`, `tail()`
- `describe()`, `info()`

### Sélection et indexation
- Sélection par nom : `df['column']`, `df.column`
- Indexation par position : `iloc[]`
- Indexation par label : `loc[]`
- Sélection conditionnelle : `df[condition]`
- Conditions multiples avec `&`, `|`, `~`

### Fonctions de résumé
- `mean()`, `median()`, `std()`
- `count()`, `nunique()`, `unique()`
- `value_counts()`
- `min()`, `max()`, `idxmin()`, `idxmax()`

### Transformation
- `map()` pour transformer une Series
- `apply()` pour transformer DataFrame/Series
- Opérations vectorisées
- Création de nouvelles colonnes

### Groupement
- `groupby()` simple et multiple
- Fonctions d'agrégation : `agg()`, `sum()`, `mean()`, etc.
- `reset_index()` pour aplatir les résultats

### Nettoyage des données
- Détection : `isnull()`, `notnull()`
- Suppression : `dropna()`
- Remplacement : `fillna()`, `replace()`

### Restructuration
- `rename()` pour colonnes et index
- `rename_axis()` pour noms d'axes
- `set_index()` pour changer l'index

## Conseils

### 💡 Bonnes pratiques
- Utilisez `df.copy()` quand vous modifiez un DataFrame
- Préférez les méthodes pandas aux boucles Python
- Exploitez les opérations vectorisées pour la performance
- Gérez les valeurs manquantes explicitement

### 🐛 Erreurs courantes
- Oublier que `iloc` utilise des positions (0-based)
- Confondre `loc` et `iloc` pour la sélection
- Ne pas gérer les valeurs manquantes (NaN)
- Modifier le DataFrame original au lieu d'une copie

### 🚀 Optimisations
- Utilisez `value_counts()` au lieu de `groupby().count()`
- Préférez les opérations vectorisées à `apply()` quand possible
- Utilisez `inplace=True` avec précaution (modifie l'original)

## Ressources supplémentaires

- [Documentation officielle Pandas](https://pandas.pydata.org/docs/)
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## Niveau de difficulté

- 🟢 **Débutant** : Exercices 1-3 (lecture, sélection de base)
- 🟡 **Intermédiaire** : Exercices 4-7 (statistiques, transformations, groupement)
- 🔴 **Avancé** : Exercices 8-10 (restructuration, analyse complexe)

Bon travail et bonne découverte de pandas ! 🐼
