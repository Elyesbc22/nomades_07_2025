"""
🎯 EXERCICES NUMPY COMPLETS
Reprend tous les concepts vus dans le cours NumPy Operations

Sections couvertes :
1. Création d'arrays et opérations arithmétiques
2. Fonctions NumPy (création, manipulation, mathématiques, statistiques)
3. Opérations de comparaison et logiques
4. Fonctions mathématiques (trigonométriques, arrondis)
5. Constantes NumPy
6. Fonctions statistiques avancées
7. Fonctions pour chaînes de caractères

💡 Instructions : Complétez les fonctions en remplaçant les 'pass' et 'None'
"""

import numpy as np

# ===============================
# SECTION 1: OPÉRATIONS ARITHMÉTIQUES
# ===============================

def exercice_1_operations_arithmetiques():
    """
    Exercice 1: Maîtriser les opérations arithmétiques element-wise
    """
    print("=== EXERCICE 1: Opérations Arithmétiques ===")
    
    # Créez deux arrays pour les tests
    array_a = np.array([10, 20, 30, 40])
    array_b = np.array([2, 4, 6, 8])
    
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    
    # 1.1 Addition avec opérateur et fonction
    # TODO: Utilisez + et np.add()
    addition_op = None
    addition_func = None
    
    # 1.2 Soustraction avec opérateur et fonction  
    # TODO: Utilisez - et np.subtract()
    soustraction_op = None
    soustraction_func = None
    
    # 1.3 Multiplication avec opérateur et fonction
    # TODO: Utilisez * et np.multiply()
    multiplication_op = None
    multiplication_func = None
    
    # 1.4 Division avec opérateur et fonction
    # TODO: Utilisez / et np.divide()
    division_op = None
    division_func = None
    
    # 1.5 Puissance avec opérateur et fonction
    # TODO: Élevez array_a à la puissance 2 avec ** et np.power()
    puissance_op = None
    puissance_func = None
    
    # 1.6 Modulo avec opérateur et fonction
    # TODO: Utilisez % et np.mod()
    modulo_op = None
    modulo_func = None
    
    # Affichage des résultats
    try:
        print(f"✅ Addition: {addition_op} = {addition_func}")
        print(f"✅ Soustraction: {soustraction_op} = {soustraction_func}")
        print(f"✅ Multiplication: {multiplication_op} = {multiplication_func}")
        print(f"✅ Division: {division_op} = {division_func}")
        print(f"✅ Puissance: {puissance_op} = {puissance_func}")
        print(f"✅ Modulo: {modulo_op} = {modulo_func}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

# ===============================
# SECTION 2: FONCTIONS DE CRÉATION ET MANIPULATION
# ===============================

def exercice_2_fonctions_creation_manipulation():
    """
    Exercice 2: Fonctions de création et manipulation d'arrays
    """
    print("\n=== EXERCICE 2: Création et Manipulation ===")
    
    # 2.1 Création d'arrays
    # TODO: Créez les arrays suivants
    array_zeros = None  # Array 3x4 de zéros
    array_ones = None   # Array 2x3 de uns
    array_range = None  # Array de 0 à 15
    array_random = None # Array 2x2 de nombres aléatoires
    
    # 2.2 Manipulation d'arrays
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    
    # TODO: Reshape data en array 3x4
    data_2d = None
    
    # TODO: Transposez data_2d
    data_transposed = None
    
    try:
        print(f"✅ Zeros shape: {array_zeros.shape}")
        print(f"✅ Ones shape: {array_ones.shape}")
        print(f"✅ Range: {array_range}")
        print(f"✅ Random shape: {array_random.shape}")
        print(f"✅ Data 2D shape: {data_2d.shape}")
        print(f"✅ Transposed shape: {data_transposed.shape}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

# ===============================
# SECTION 3: OPÉRATIONS DE COMPARAISON ET LOGIQUES
# ===============================

def exercice_3_comparaison_logique():
    """
    Exercice 3: Opérations de comparaison et logiques
    """
    print("\n=== EXERCICE 3: Comparaison et Logique ===")
    
    array1 = np.array([1, 5, 3, 8, 2])
    array2 = np.array([2, 4, 3, 6, 7])
    
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")
    
    # 3.1 Comparaisons avec opérateurs
    # TODO: Utilisez les opérateurs <, >, ==, !=
    moins_que = None
    plus_que = None
    egal = None
    different = None
    
    # 3.2 Comparaisons avec fonctions
    # TODO: Utilisez np.less(), np.greater(), np.equal(), np.not_equal()
    moins_que_func = None
    plus_que_func = None
    egal_func = None
    different_func = None
    
    # 3.3 Opérations logiques
    bool_array1 = np.array([True, False, True, False])
    bool_array2 = np.array([False, False, True, True])
    
    # TODO: Utilisez np.logical_and(), np.logical_or(), np.logical_not()
    logical_and = None
    logical_or = None
    logical_not = None
    
    try:
        print(f"✅ Moins que: {moins_que}")
        print(f"✅ Plus que: {plus_que}")
        print(f"✅ Égal: {egal}")
        print(f"✅ Différent: {different}")
        print(f"✅ AND: {logical_and}")
        print(f"✅ OR: {logical_or}")
        print(f"✅ NOT: {logical_not}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

# ===============================
# SECTION 4: FONCTIONS MATHÉMATIQUES
# ===============================

def exercice_4_fonctions_mathematiques():
    """
    Exercice 4: Fonctions mathématiques (trigonométriques, arrondis)
    """
    print("\n=== EXERCICE 4: Fonctions Mathématiques ===")
    
    # 4.1 Fonctions trigonométriques
    angles_rad = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
    angles_deg = np.array([0, 30, 45, 60, 90])
    
    # TODO: Calculez sin, cos, tan des angles en radians
    sin_vals = None
    cos_vals = None
    tan_vals = None
    
    # TODO: Convertissez angles_deg en radians et angles_rad en degrés
    deg_to_rad = None
    rad_to_deg = None
    
    # 4.2 Fonctions d'arrondi
    decimals = np.array([1.23456, 2.67891, 3.14159, 4.99999])
    
    # TODO: Utilisez np.round(), np.floor(), np.ceil()
    rounded_2_dec = None  # Arrondi à 2 décimales
    floor_vals = None     # Arrondi vers le bas
    ceil_vals = None      # Arrondi vers le haut
    
    try:
        print(f"✅ Sinus: {sin_vals}")
        print(f"✅ Cosinus: {cos_vals}")
        print(f"✅ Degrés vers radians: {deg_to_rad}")
        print(f"✅ Arrondi 2 décimales: {rounded_2_dec}")
        print(f"✅ Floor: {floor_vals}")
        print(f"✅ Ceil: {ceil_vals}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

# ===============================
# SECTION 5: CONSTANTES NUMPY
# ===============================

def exercice_5_constantes():
    """
    Exercice 5: Utilisation des constantes NumPy
    """
    print("\n=== EXERCICE 5: Constantes NumPy ===")
    
    # 5.1 Calculs avec pi
    rayon = 5
    # TODO: Calculez la circonférence et l'aire d'un cercle
    circonference = None  # 2 * pi * rayon
    aire = None          # pi * rayon²
    
    # 5.2 Calculs avec e
    x = 2
    # TODO: Calculez e^x et utilisez la constante e
    exp_x = None         # e^x avec np.exp()
    e_constant = None    # La valeur de e
    
    # 5.3 Opérations avec constantes et arrays
    array_vals = np.array([1, 2, 3, 4])
    # TODO: Ajoutez pi à chaque élément, multipliez par e
    array_plus_pi = None
    array_fois_e = None
    
    try:
        print(f"✅ Circonférence (r={rayon}): {circonference:.2f}")
        print(f"✅ Aire (r={rayon}): {aire:.2f}")
        print(f"✅ e^{x}: {exp_x:.2f}")
        print(f"✅ Constante e: {e_constant:.2f}")
        print(f"✅ Array + π: {array_plus_pi}")
        print(f"✅ Array × e: {array_fois_e}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

# ===============================
# SECTION 6: FONCTIONS STATISTIQUES
# ===============================

def exercice_6_statistiques():
    """
    Exercice 6: Fonctions statistiques avancées
    """
    print("\n=== EXERCICE 6: Statistiques ===")
    
    # Données pour les tests
    notes = np.array([12, 15, 18, 14, 16, 13, 17, 19, 11, 20])
    matrix_data = np.array([[10, 20, 30], 
                           [40, 50, 60], 
                           [70, 80, 90]])
    
    print(f"Notes: {notes}")
    print(f"Matrix:\n{matrix_data}")
    
    # 6.1 Statistiques de base sur notes
    # TODO: Calculez moyenne, médiane, écart-type, variance
    moyenne = None
    mediane = None
    ecart_type = None
    variance = None
    min_val = None
    max_val = None
    
    # 6.2 Percentiles
    # TODO: Calculez les 25e, 50e, 75e percentiles
    p25 = None
    p50 = None
    p75 = None
    
    # 6.3 Statistiques sur matrix 2D
    # TODO: Calculez la moyenne par ligne (axis=1) et par colonne (axis=0)
    moyenne_lignes = None
    moyenne_colonnes = None
    
    # TODO: Calculez l'écart-type de toute la matrice
    ecart_type_total = None
    
    try:
        print(f"✅ Moyenne: {moyenne:.2f}")
        print(f"✅ Médiane: {mediane:.2f}")
        print(f"✅ Écart-type: {ecart_type:.2f}")
        print(f"✅ Min/Max: {min_val}/{max_val}")
        print(f"✅ Percentiles (25,50,75): {p25}, {p50}, {p75}")
        print(f"✅ Moyenne par lignes: {moyenne_lignes}")
        print(f"✅ Moyenne par colonnes: {moyenne_colonnes}")
        print(f"✅ Écart-type total: {ecart_type_total:.2f}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

# ===============================
# SECTION 7: FONCTIONS CHAÎNES DE CARACTÈRES
# ===============================

def exercice_7_chaines_caracteres():
    """
    Exercice 7: Manipulation de chaînes avec NumPy
    """
    print("\n=== EXERCICE 7: Chaînes de Caractères ===")
    
    # 7.1 Manipulation de base
    prenoms = np.array(['alice', 'bob', 'charlie'])
    noms = np.array(['dupont', 'martin', 'durand'])
    
    # TODO: Utilisez les fonctions de chaînes NumPy
    prenoms_maj = None        # Première lettre en majuscule
    noms_upper = None         # Tout en majuscules
    noms_lower = None         # Tout en minuscules
    
    # 7.2 Concaténation et répétition
    # TODO: Concaténez prenoms et noms avec un espace
    noms_complets = None      # Utilisez np.char.add()
    
    # TODO: Répétez chaque prénom 3 fois
    prenoms_repetes = None    # Utilisez np.char.multiply()
    
    # 7.3 Comparaison et jointure
    lang1 = np.array(['Python', 'Java', 'C++'])
    lang2 = np.array(['Python', 'JavaScript', 'C++'])
    
    # TODO: Comparez les deux arrays élément par élément
    langages_egaux = None     # Utilisez np.char.equal()
    
    # TODO: Joignez les caractères avec '-'
    lang_joined = None        # Utilisez np.char.join()
    
    try:
        print(f"✅ Prénoms capitalisés: {prenoms_maj}")
        print(f"✅ Noms majuscules: {noms_upper}")
        print(f"✅ Noms complets: {noms_complets}")
        print(f"✅ Prénoms répétés: {prenoms_repetes}")
        print(f"✅ Langages égaux: {langages_egaux}")
        print(f"✅ Langages joints: {lang_joined}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

# ===============================
# EXERCICE BONUS: PROJET INTÉGRÉ
# ===============================

def exercice_bonus_projet_integre():
    """
    Exercice Bonus: Projet intégrant tous les concepts
    Analysez un dataset de températures
    """
    print("\n=== EXERCICE BONUS: Analyse de Températures ===")
    
    # Simulation de données météo (températures en °C sur 30 jours)
    np.random.seed(42)
    temperatures = np.random.normal(20, 5, 30)  # Moyenne 20°C, écart-type 5°C
    villes = np.array(['Paris', 'Lyon', 'Marseille'])
    
    print(f"Températures (30 jours): {temperatures[:10]}... (10 premiers)")
    
    # TODO: Répondez aux questions suivantes
    
    # 1. Statistiques de base
    temp_moyenne = None
    temp_mediane = None
    temp_min = None
    temp_max = None
    temp_ecart_type = None
    
    # 2. Conversions
    # TODO: Convertissez en Fahrenheit (F = C * 9/5 + 32)
    temperatures_f = None
    
    # 3. Analyse conditionnelle
    # TODO: Trouvez les jours où temp > moyenne + écart-type (jours chauds)
    jours_chauds = None
    nb_jours_chauds = None
    
    # 4. Transformations mathématiques
    # TODO: Appliquez une fonction trigonométrique pour modéliser une variation saisonnière
    jours = np.arange(1, 31)
    variation_saisonniere = None  # Utilisez np.sin() avec les jours
    
    # 5. Arrondis et formatage
    # TODO: Arrondissez les températures à 1 décimale
    temperatures_arrondies = None
    
    # 6. Analyse des extrêmes
    # TODO: Trouvez les indices des températures min et max
    indice_temp_min = None
    indice_temp_max = None
    
    try:
        print(f"✅ Température moyenne: {temp_moyenne:.1f}°C")
        print(f"✅ Température médiane: {temp_mediane:.1f}°C")
        print(f"✅ Min/Max: {temp_min:.1f}°C / {temp_max:.1f}°C")
        print(f"✅ Écart-type: {temp_ecart_type:.1f}°C")
        print(f"✅ Température max en Fahrenheit: {temperatures_f[indice_temp_max]:.1f}°F")
        print(f"✅ Nombre de jours chauds: {nb_jours_chauds}")
        print(f"✅ Jour le plus froid: jour {indice_temp_min + 1}")
        print(f"✅ Jour le plus chaud: jour {indice_temp_max + 1}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

# ===============================
# SOLUTIONS (à décommenter pour voir les réponses)
# ===============================

def afficher_solutions():
    """
    Affiche toutes les solutions des exercices
    """
    print("\n" + "="*60)
    print("🔥 SOLUTIONS DES EXERCICES 🔥")
    print("="*60)
    
    solutions = """
    EXERCICE 1 - SOLUTIONS:
    addition_op = array_a + array_b
    addition_func = np.add(array_a, array_b)
    soustraction_op = array_a - array_b
    soustraction_func = np.subtract(array_a, array_b)
    multiplication_op = array_a * array_b
    multiplication_func = np.multiply(array_a, array_b)
    division_op = array_a / array_b
    division_func = np.divide(array_a, array_b)
    puissance_op = array_a ** 2
    puissance_func = np.power(array_a, 2)
    modulo_op = array_a % array_b
    modulo_func = np.mod(array_a, array_b)
    
    EXERCICE 2 - SOLUTIONS:
    array_zeros = np.zeros((3, 4))
    array_ones = np.ones((2, 3))
    array_range = np.arange(16)
    array_random = np.random.rand(2, 2)
    data_2d = data.reshape(3, 4)
    data_transposed = data_2d.T  # ou np.transpose(data_2d)
    
    EXERCICE 3 - SOLUTIONS:
    moins_que = array1 < array2
    plus_que = array1 > array2
    egal = array1 == array2
    different = array1 != array2
    moins_que_func = np.less(array1, array2)
    plus_que_func = np.greater(array1, array2)
    egal_func = np.equal(array1, array2)
    different_func = np.not_equal(array1, array2)
    logical_and = np.logical_and(bool_array1, bool_array2)
    logical_or = np.logical_or(bool_array1, bool_array2)
    logical_not = np.logical_not(bool_array1)
    
    EXERCICE 4 - SOLUTIONS:
    sin_vals = np.sin(angles_rad)
    cos_vals = np.cos(angles_rad)
    tan_vals = np.tan(angles_rad)
    deg_to_rad = np.radians(angles_deg)
    rad_to_deg = np.degrees(angles_rad)
    rounded_2_dec = np.round(decimals, 2)
    floor_vals = np.floor(decimals)
    ceil_vals = np.ceil(decimals)
    
    EXERCICE 5 - SOLUTIONS:
    circonference = 2 * np.pi * rayon
    aire = np.pi * rayon**2
    exp_x = np.exp(x)
    e_constant = np.e
    array_plus_pi = array_vals + np.pi
    array_fois_e = array_vals * np.e
    
    EXERCICE 6 - SOLUTIONS:
    moyenne = np.mean(notes)
    mediane = np.median(notes)
    ecart_type = np.std(notes)
    variance = np.var(notes)
    min_val = np.min(notes)
    max_val = np.max(notes)
    p25 = np.percentile(notes, 25)
    p50 = np.percentile(notes, 50)
    p75 = np.percentile(notes, 75)
    moyenne_lignes = np.mean(matrix_data, axis=1)
    moyenne_colonnes = np.mean(matrix_data, axis=0)
    ecart_type_total = np.std(matrix_data)
    
    EXERCICE 7 - SOLUTIONS:
    prenoms_maj = np.char.capitalize(prenoms)
    noms_upper = np.char.upper(noms)
    noms_lower = np.char.lower(noms)
    noms_complets = np.char.add(np.char.add(prenoms_maj, ' '), noms_upper)
    prenoms_repetes = np.char.multiply(prenoms, 3)
    langages_egaux = np.char.equal(lang1, lang2)
    lang_joined = np.char.join('-', lang1)
    
    EXERCICE BONUS - SOLUTIONS:
    temp_moyenne = np.mean(temperatures)
    temp_mediane = np.median(temperatures)
    temp_min = np.min(temperatures)
    temp_max = np.max(temperatures)
    temp_ecart_type = np.std(temperatures)
    temperatures_f = temperatures * 9/5 + 32
    seuil_chaud = temp_moyenne + temp_ecart_type
    jours_chauds = temperatures > seuil_chaud
    nb_jours_chauds = np.sum(jours_chauds)
    variation_saisonniere = np.sin(jours * 2 * np.pi / 365)
    temperatures_arrondies = np.round(temperatures, 1)
    indice_temp_min = np.argmin(temperatures)
    indice_temp_max = np.argmax(temperatures)
    """
    
    print(solutions)

# ===============================
# FONCTION PRINCIPALE
# ===============================

def main():
    """
    Lance tous les exercices NumPy complets
    """
    print("🎯 EXERCICES NUMPY COMPLETS 🎯")
    print("📚 Révision complète du cours NumPy Operations")
    print("💡 Remplacez les 'None' et 'pass' par votre code")
    print("📖 Tapez 'afficher_solutions()' pour voir les réponses\n")
    
    # Lance tous les exercices
    exercice_1_operations_arithmetiques()
    exercice_2_fonctions_creation_manipulation()
    exercice_3_comparaison_logique()
    exercice_4_fonctions_mathematiques()
    exercice_5_constantes()
    exercice_6_statistiques()
    exercice_7_chaines_caracteres()
    exercice_bonus_projet_integre()
    
    print("\n🎉 Tous les exercices sont disponibles ! 🎉")
    print("💡 Pour voir les solutions, appelez: afficher_solutions()")

def solutions():
    """Raccourci pour afficher les solutions"""
    afficher_solutions()

if __name__ == "__main__":
    main()
