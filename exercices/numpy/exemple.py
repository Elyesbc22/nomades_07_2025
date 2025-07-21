import numpy as np

def exercice_1_creation_arrays():
    """
    Exercice 1: Création d'arrays basiques
    Complétez les TODO ci-dessous
    """
    print("=== Exercice 1: Création d'Arrays ===")
    
    # 1.1 Créez un array à partir d'une liste [1, 2, 3, 4, 5]
    
    # TODO: Remplacez None par votre code
    array1 = np.arange(1, 6)
    
    # 1.2 Créez un array de 8 zéros
    # TODO: Remplacez None par votre code
    array_zeros = np.zeros(8)
    
    # 1.3 Créez un array de 5 uns
    # TODO: Remplacez None par votre code
    array_ones = np.ones((5,))
    
    # 1.4 Créez un array avec les nombres de 0 à 9
    # TODO: Remplacez None par votre code
    array_range = np.arange(10)
    
    # 1.5 Créez un array avec les nombres de 2 à 20 par pas de 2
    # TODO: Remplacez None par votre code
    array_step = np.arange(2, 21, 2)
    
    # 1.6 Créez un array de 6 nombres aléatoires entre 0 et 1
    # TODO: Remplacez None par votre code
    array_random = np.random.rand(6)
    
    # Vérification (ne pas modifier)
    try:
        print(f"✅ Array simple: {array1}")
        print(f"✅ Array de zéros: {array_zeros}")
        print(f"✅ Array de uns: {array_ones}")
        print(f"✅ Array range: {array_range}")
        print(f"✅ Array par pas: {array_step}")
        print(f"✅ Array aléatoire: {array_random}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

def exercice_2_arrays_2d():
    """
    Exercice 2: Création d'arrays 2D et 3D
    """
    print("\n=== Exercice 2: Arrays 2D et 3D ===")
    
    # 2.1 Créez un array 2D de shape (3, 4) rempli de zéros
    # TODO: Remplacez None
    array_2d_zeros = np.zeros((3, 4))
    
    # 2.2 Créez un array 2D de shape (2, 5) rempli de 7
    # TODO: Remplacez None
    array_2d_seven = np.full((2, 5), 7)
    
    # 2.3 Créez un array 2D à partir de cette liste de listes:
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # TODO: Remplacez None
    
    array_2d_list = np.empty((3,3))
    for i in range(1, 4):
        array_2d_list[0, i-1] = i
        array_2d_list[1, i-1] = i+3
        array_2d_list[2, i-1] = i+6
    
    # 2.4 Créez un array 3D de shape (2, 2, 3) rempli de uns
    # TODO: Remplacez None
    array_3d_ones = np.ones((2,2,3))
    
    # 2.5 Créez un array 2D de shape (3, 3) avec des nombres aléatoires
    # TODO: Remplacez None
    array_2d_random = np.random.rand(3,3)
    
    # Vérification
    try:
        print(f"✅ Array 2D zeros - Shape: {array_2d_zeros.shape}")
        print(f"✅ Array 2D sevens:\n{array_2d_seven}")
        print(f"✅ Array 2D from list:\n{array_2d_list}")
        print(f"✅ Array 3D ones - Shape: {array_3d_ones.shape}")
        print(f"✅ Array 2D random - Shape: {array_2d_random.shape}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

def exercice_3_indexation_1d():
    """
    Exercice 3: Indexation sur arrays 1D
    """
    print("\n=== Exercice 3: Indexation 1D ===")
    
    # Array de base pour les exercices
    numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(f"Array de base: {numbers}")
    
    # 3.1 Accédez au premier élément
    # TODO: Remplacez None
    premier = None
    
    # 3.2 Accédez au dernier élément
    # TODO: Remplacez None
    dernier = None
    
    # 3.3 Accédez au 5ème élément (index 4)
    # TODO: Remplacez None
    cinquieme = None
    
    # 3.4 Accédez au 3ème élément en partant de la fin
    # TODO: Remplacez None
    troisieme_fin = None
    
    # 3.5 Modifiez le 2ème élément (index 1) pour qu'il vaille 25
    # TODO: Complétez cette ligne
    # numbers[?] = 25
    
    # 3.6 Modifiez le dernier élément pour qu'il vaille 95
    # TODO: Complétez cette ligne
    # numbers[?] = 95
    
    # Vérification
    try:
        print(f"✅ Premier élément: {premier}")
        print(f"✅ Dernier élément: {dernier}")
        print(f"✅ 5ème élément: {cinquieme}")
        print(f"✅ 3ème depuis la fin: {troisieme_fin}")
        print(f"✅ Array modifié: {numbers}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

def exercice_4_slicing_1d():
    """
    Exercice 4: Slicing sur arrays 1D
    """
    print("\n=== Exercice 4: Slicing 1D ===")
    
    # Array de base
    data = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    print(f"Array de base: {data}")
    
    # 4.1 Récupérez les 5 premiers éléments
    # TODO: Remplacez None
    premiers_5 = None
    
    # 4.2 Récupérez les 3 derniers éléments
    # TODO: Remplacez None
    derniers_3 = None
    
    # 4.3 Récupérez les éléments de l'index 2 à 7 (exclus)
    # TODO: Remplacez None
    milieu = None
    
    # 4.4 Récupérez un élément sur deux (tous les indices pairs)
    # TODO: Remplacez None
    pairs = None
    
    # 4.5 Récupérez un élément sur trois en commençant par l'index 1
    # TODO: Remplacez None
    un_sur_trois = None
    
    # 4.6 Récupérez l'array dans l'ordre inverse
    # TODO: Remplacez None
    inverse = None
    
    # 4.7 Modifiez les éléments de l'index 3 à 6 (exclus) pour qu'ils valent 99
    # TODO: Complétez cette ligne
    # data[?:?] = 99
    
    # Vérification
    try:
        print(f"✅ 5 premiers: {premiers_5}")
        print(f"✅ 3 derniers: {derniers_3}")
        print(f"✅ Milieu (index 2-6): {milieu}")
        print(f"✅ Indices pairs: {pairs}")
        print(f"✅ Un sur trois: {un_sur_trois}")
        print(f"✅ Ordre inverse: {inverse}")
        print(f"✅ Array modifié: {data}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

def exercice_5_indexation_2d():
    """
    Exercice 5: Indexation sur arrays 2D
    """
    print("\n=== Exercice 5: Indexation 2D ===")
    
    # Array 2D de base
    matrix = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12]])
    print(f"Matrice de base:\n{matrix}")
    
    # 5.1 Accédez à l'élément de la 2ème ligne, 3ème colonne (indices 1, 2)
    # TODO: Remplacez None
    element = None
    
    # 5.2 Accédez à toute la première ligne
    # TODO: Remplacez None
    premiere_ligne = matrix[-1]
    
    # 5.3 Accédez à toute la dernière colonne
    # TODO: Remplacez None
    derniere_colonne = matrix[:, -1] 
    
    # 5.4 Accédez à l'élément en bas à droite
    # TODO: Remplacez None
    coin_bas_droite = None
    
    # 5.5 Modifiez l'élément de la 1ère ligne, 2ème colonne pour qu'il vaille 99
    # TODO: Complétez cette ligne
    # matrix[?, ?] = 99
    
    # 5.6 Modifiez toute la dernière ligne pour qu'elle vaille [100, 101, 102, 103]
    # TODO: Complétez cette ligne
    # matrix[?, :] = [100, 101, 102, 103]
    
    # Vérification
    try:
        print(f"✅ Élément (ligne 2, col 3): {element}")
        print(f"✅ Première ligne: {premiere_ligne}")
        print(f"✅ Dernière colonne: {derniere_colonne}")
        print(f"✅ Coin bas-droite: {coin_bas_droite}")
        print(f"✅ Matrice modifiée:\n{matrix}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

def exercice_6_slicing_2d():
    """
    Exercice 6: Slicing sur arrays 2D
    """
    print("\n=== Exercice 6: Slicing 2D ===")
    
    # Array 2D de base
    grid = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20]])
    print(f"Grille de base:\n{grid}")
    
    # 6.1 Récupérez les 2 premières lignes et 3 premières colonnes
    # TODO: Remplacez None
    coin_haut_gauche = None
    
    # 6.2 Récupérez les 2 dernières lignes et 2 dernières colonnes
    # TODO: Remplacez None
    coin_bas_droite = None
    
    # 6.3 Récupérez les lignes du milieu (indices 1 et 2)
    # TODO: Remplacez None
    lignes_milieu = None
    
    # 6.4 Récupérez une ligne sur deux et une colonne sur deux
    # TODO: Remplacez None
    damier = None
    
    # 6.5 Modifiez le carré central (lignes 1-2, colonnes 1-3) pour qu'il vaille 0
    # TODO: Complétez cette ligne
    # grid[?:?, ?:?] = 0
    
    # Vérification
    try:
        print(f"✅ Coin haut-gauche (2x3):\n{coin_haut_gauche}")
        print(f"✅ Coin bas-droite (2x2):\n{coin_bas_droite}")
        print(f"✅ Lignes du milieu:\n{lignes_milieu}")
        print(f"✅ Damier:\n{damier}")
        print(f"✅ Grille modifiée:\n{grid}")
    except:
        print("❌ Il y a encore des TODO à compléter!")

def afficher_solutions():
    """
    Affiche toutes les solutions des exercices
    """
    print("\n" + "="*60)
    print("🔥 SOLUTIONS DES EXERCICES 🔥")
    print("="*60)
    
    print("\n=== SOLUTION Exercice 1 ===")
    print("array1 = np.array([1, 2, 3, 4, 5])")
    print("array_zeros = np.zeros(8)")
    print("array_ones = np.ones(5)")
    print("array_range = np.arange(10)")
    print("array_step = np.arange(2, 21, 2)")
    print("array_random = np.random.rand(6)")
    
    print("\n=== SOLUTION Exercice 2 ===")
    print("array_2d_zeros = np.zeros((3, 4))")
    print("array_2d_seven = np.full((2, 5), 7)")
    print("array_2d_list = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])")
    print("array_3d_ones = np.ones((2, 2, 3))")
    print("array_2d_random = np.random.rand(3, 3)")
    
    print("\n=== SOLUTION Exercice 3 ===")
    print("premier = numbers[0]")
    print("dernier = numbers[-1]")
    print("cinquieme = numbers[4]")
    print("troisieme_fin = numbers[-3]")
    print("numbers[1] = 25")
    print("numbers[-1] = 95")
    
    print("\n=== SOLUTION Exercice 4 ===")
    print("premiers_5 = data[:5]")
    print("derniers_3 = data[-3:]")
    print("milieu = data[2:7]")
    print("pairs = data[::2]")
    print("un_sur_trois = data[1::3]")
    print("inverse = data[::-1]")
    print("data[3:6] = 99")
    
    print("\n=== SOLUTION Exercice 5 ===")
    print("element = matrix[1, 2]")
    print("premiere_ligne = matrix[0, :]")
    print("derniere_colonne = matrix[:, -1]")
    print("coin_bas_droite = matrix[-1, -1]")
    print("matrix[0, 1] = 99")
    print("matrix[-1, :] = [100, 101, 102, 103]")
    
    print("\n=== SOLUTION Exercice 6 ===")
    print("coin_haut_gauche = grid[:2, :3]")
    print("coin_bas_droite = grid[-2:, -2:]")
    print("lignes_milieu = grid[1:3, :]")
    print("damier = grid[::2, ::2]")
    print("grid[1:3, 1:4] = 0")

def main():
    """
    Lance tous les exercices NumPy
    """
    print("🎯 EXERCICES NUMPY - CRÉATION ET INDEXATION 🎯")
    print("💡 Remplacez les 'None' et complétez les lignes commentées")
    print("📖 Tapez 'solutions()' pour voir les réponses\n")
    
    # Lance tous les exercices
    exercice_1_creation_arrays()
    exercice_2_arrays_2d()
    exercice_3_indexation_1d()
    exercice_4_slicing_1d()
    exercice_5_indexation_2d()
    exercice_6_slicing_2d()
    
    print("\n🎉 Exercices terminés ! 🎉")
    print("💡 Pour voir les solutions, appelez: afficher_solutions()")

def solutions():
    """Raccourci pour afficher les solutions"""
    afficher_solutions()

if __name__ == "__main__":
    main()