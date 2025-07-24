# Exercices Matplotlib + Pandas

Ce dossier contient des exercices pratiques pour apprendre à utiliser **Matplotlib** avec **Pandas** pour la visualisation de données.

## 📁 Fichiers

- `exercice_matplotlib_pandas.py` - **Exercices à compléter** (version étudiante)
- `correction_exercice_matplotlib.py` - **Solutions complètes** (version corrigée)
- `README.md` - Ce fichier d'instructions

## 📊 Dataset utilisé

Les exercices utilisent le dataset des vins (`winemag-data-130k-v2.csv`) qui contient :
- **Colonnes principales** : points, price, country, variety, title, description
- **130 000+ lignes** de données sur différents vins
- **Objectif** : Analyser et visualiser les tendances des vins dans le monde

## 🎯 Exercices à réaliser

### Exercice 1: Chargement des données
- Charger le CSV avec pandas
- Nettoyer les données de prix (remplacer NaN par la médiane)
- Afficher les informations de base

### Exercice 2: Histogramme 📊
- Créer un histogramme de la distribution des points
- Utiliser 20 bins, couleur bleue avec transparence
- Ajouter titre, labels et sauvegarder

### Exercice 3: Scatter Plot 📈
- Diagramme de dispersion prix vs points
- Filtrer les prix < 200$ pour éviter les outliers
- Points verts avec transparence

### Exercice 4: Graphique en barres 📊
- Top 10 des pays producteurs
- Barres horizontales en rouge
- Labels et titre appropriés

### Exercice 5: Diagramme circulaire 🥧
- 8 variétés de vin les plus communes
- Pourcentages affichés
- Première tranche "explosée"

### Exercice 6: Subplots multiples 📋
- Figure 2x2 avec 4 graphiques différents
- Histogramme points, scatter plot, barres pays, distribution prix
- Sauvegarde sous 'analyse_complete.png'

### Exercice 7: Régression linéaire 📉
- Analyse avancée prix vs points
- Filtrage des données (prix 10-100$, points 80-100)
- Ligne de régression avec équation dans le titre

### Exercice 8: Box plot 📦
- Distribution des prix par catégories de notes
- Catégories : Excellent (≥95), Très bon (90-94), Bon (85-89), Moyen (<85)
- Limiter prix < 200$ pour lisibilité

## 🎁 Exercices Bonus

### Bonus 1: Graphique 3D
- Utiliser `plt.subplot(projection='3d')`
- Axes : points, prix, index

### Bonus 2: Heatmap de corrélation
- Matrice de corrélation avec `plt.imshow()`
- Variables numériques du dataset

### Bonus 3: Styles personnalisés
- Tester différents styles matplotlib
- 'default', 'ggplot', 'seaborn', 'dark_background'

## 🚀 Comment commencer

### 1. Vérifier les dépendances
```bash
# Installer les packages nécessaires
conda install matplotlib pandas numpy
# ou
pip install matplotlib pandas numpy
```

### 2. Vérifier le chemin des données
```python
# Le fichier doit être accessible à :
file_path = r"..\..\data\pandas\winemag-data-130k-v2.csv"
```

### 3. Commencer par les exercices
```bash
# Ouvrir le fichier d'exercices
code exercice_matplotlib_pandas.py

# Compléter les méthodes marquées "TODO:"
# Tester chaque exercice individuellement
```

### 4. Vérifier avec la correction
```bash
# Exécuter la correction pour voir les solutions
python correction_exercice_matplotlib.py
```

## 📚 Concepts Matplotlib utilisés

| Fonction | Usage | Exercice |
|----------|-------|----------|
| `plt.hist()` | Histogrammes | Ex. 2, 6 |
| `plt.scatter()` | Diagrammes de dispersion | Ex. 3, 6, 7 |
| `plt.bar()` / `plt.barh()` | Graphiques en barres | Ex. 4, 6 |
| `plt.pie()` | Diagrammes circulaires | Ex. 5 |
| `plt.subplot()` | Graphiques multiples | Ex. 6 |
| `plt.plot()` | Lignes (régression) | Ex. 7 |
| `plt.boxplot()` | Box plots | Ex. 8 |
| `plt.title()`, `plt.xlabel()`, `plt.ylabel()` | Labels | Tous |
| `plt.savefig()` | Sauvegarde | Ex. 2, 6 |
| `plt.grid()` | Grille | Ex. 7 |
| `plt.style.use()` | Styles | Bonus 3 |

## 📈 Fonctionnalités Pandas utilisées

| Méthode | Usage | Exercice |
|---------|-------|----------|
| `pd.read_csv()` | Chargement données | Ex. 1 |
| `df.fillna()` | Nettoyage NaN | Ex. 1 |
| `df.value_counts()` | Comptages | Ex. 4, 5 |
| `df[condition]` | Filtrage | Ex. 3, 6, 7, 8 |
| `df.apply()` | Transformation | Ex. 8 |
| `df.corr()` | Corrélation | Bonus 2 |
| `df.sample()` | Échantillonnage | Bonus 1 |

## 🎨 Types de graphiques créés

1. **📊 Histogramme** - Distribution des points
2. **📈 Scatter plot** - Relation prix/points
3. **📊 Barres horizontales** - Top pays
4. **🥧 Diagramme circulaire** - Variétés de vin
5. **📋 Subplots 2x2** - Vue d'ensemble
6. **📉 Régression linéaire** - Tendance prix/points
7. **📦 Box plot** - Distribution par catégorie
8. **🌐 3D** - Analyse tridimensionnelle (bonus)
9. **🔥 Heatmap** - Corrélations (bonus)

## 💡 Conseils

### Pour débuter
- Commencez par l'exercice 1 (chargement des données)
- Testez chaque méthode individuellement
- Utilisez `df.head()`, `df.info()` pour explorer les données

### Pour les graphiques
- Toujours ajouter titre et labels
- Utiliser `plt.tight_layout()` pour les subplots
- Ajuster la taille avec `plt.figure(figsize=(width, height))`
- Sauvegarder avec `dpi=300` pour la qualité

### Pour le débogage
- Vérifier les types de données avec `df.dtypes`
- Filtrer les NaN avec `df.dropna()`
- Utiliser `print()` pour vérifier les valeurs intermédiaires

## 🏆 Objectifs d'apprentissage

À la fin de ces exercices, vous devrez savoir :
- ✅ Charger et nettoyer des données avec Pandas
- ✅ Créer 6+ types de graphiques différents
- ✅ Personnaliser l'apparence des graphiques
- ✅ Combiner plusieurs graphiques avec subplots
- ✅ Sauvegarder les visualisations
- ✅ Analyser des relations dans les données
- ✅ Utiliser des styles et thèmes

## 📞 Aide

Si vous êtes bloqué :
1. **Consulter le cours** `33_matplotlib.ipynb`
2. **Regarder la correction** `correction_exercice_matplotlib.py`
3. **Documentation** : [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
4. **Pandas** : [Documentation](https://pandas.pydata.org/docs/)

---

**Bon apprentissage ! 🚀📊**
