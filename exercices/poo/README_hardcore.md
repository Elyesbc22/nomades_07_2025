# Exercice: Liste Chaînée avec Programmation Orientée Objet

## Description

Cet exercice propose une implémentation complète d'une **liste chaînée** en utilisant tous les concepts de **Programmation Orientée Objet (POO)** vus en cours. C'est un excellent moyen de consolider les apprentissages théoriques avec une application pratique.

Niveau = difficile

## Objectifs pédagogiques

L'exercice permet de mettre en pratique les concepts suivants :

### 1. **Classes et Objets**
- Création de classes `Node`, `LinkedList`, `DoublyNode`, `DoublyLinkedList`
- Instanciation d'objets et utilisation de leurs méthodes

### 2. **Encapsulation**
- Utilisation d'attributs privés (`__data`, `__next`, `__head`, `__size`)
- Protection des données internes de la classe
- Validation des entrées via les setters

### 3. **Propriétés (@property)**
- Getters et setters pour contrôler l'accès aux attributs
- Propriétés calculées (`magnitude`, `is_empty`)
- Validation des données lors de l'assignation

### 4. **Méthodes spéciales (Magic Methods)**
- `__init__()` : Construction d'objets
- `__str__()` et `__repr__()` : Représentation textuelle
- `__len__()` : Support de la fonction `len()`
- `__iter__()` : Rendre les objets itérables
- `__getitem__()` et `__setitem__()` : Accès par index `[]`
- `__contains__()` : Support de l'opérateur `in`
- `__eq__()` : Comparaison d'égalité

### 5. **Héritage**
- `DoublyNode` hérite de `Node`
- `DoublyLinkedList` hérite de `LinkedList`
- Utilisation de `super()` pour appeler les méthodes parentes

### 6. **Surcharge de méthodes (Method Overriding)**
- Redéfinition des méthodes `append()` et `prepend()` dans la classe fille
- Adaptation du comportement selon le type de liste

### 7. **Méthodes statiques (@staticmethod)**
- `merge_sorted()` : Fusion de deux listes triées
- `distance()` : Calcul de distance entre vecteurs

### 8. **Polymorphisme**
- Les objets `LinkedList` et `DoublyLinkedList` peuvent être utilisés de manière similaire
- Interface commune malgré des implémentations différentes

## Structure de l'exercice

### Fichiers fournis

1. **`ex_linked_list.py`** : Fichier d'exercice avec les TODO à compléter
2. **`correction_linked_list.py`** : Correction complète de l'exercice

### Classes à implémenter

#### 1. `Node`
- Représente un nœud simple dans une liste chaînée
- Attributs : `data` (données), `next` (nœud suivant)
- Méthodes : getters/setters avec validation

#### 2. `LinkedList`
- Implémentation d'une liste chaînée simple
- Méthodes principales :
  - `append()`, `prepend()`, `insert()`
  - `remove()`, `remove_at()`, `find()`
  - `clear()`, `reverse()`
  - Support des opérateurs `[]`, `in`, `len()`, `==`
  - Itération avec `for` loop

#### 3. `DoublyNode` (héritage)
- Hérite de `Node`
- Ajoute un attribut `prev` (nœud précédent)

#### 4. `DoublyLinkedList` (héritage)
- Hérite de `LinkedList`
- Surcharge `append()` et `prepend()` pour gérer les liens bidirectionnels
- Ajoute `reverse_iterate()` pour parcourir en sens inverse

## Fonctionnalités implémentées

### Opérations de base
- ✅ Ajout d'éléments (début, fin, position)
- ✅ Suppression d'éléments (par valeur, par index)
- ✅ Recherche d'éléments
- ✅ Accès par index
- ✅ Modification par index

### Opérations avancées
- ✅ Inversion de la liste
- ✅ Fusion de listes triées
- ✅ Itération normale et inverse
- ✅ Comparaison de listes
- ✅ Gestion d'erreurs avec exceptions

### Support des opérateurs Python
```python
# Création
ll = LinkedList()

# Ajout d'éléments
ll.append("A")
ll.append("B")

# Accès par index
print(ll[0])  # "A"

# Modification
ll[1] = "C"

# Test d'appartenance
if "A" in ll:
    print("Trouvé!")

# Taille
print(len(ll))  # 2

# Itération
for item in ll:
    print(item)

# Comparaison
ll2 = LinkedList()
ll2.append("A")
ll2.append("C")
print(ll == ll2)  # True
```

## Tests inclus

Le fichier de correction inclut des tests complets qui démontrent :

1. **Création et manipulation** de nœuds
2. **Opérations CRUD** sur les listes
3. **Validation des erreurs** et gestion d'exceptions
4. **Héritage et polymorphisme** avec les listes doublement chaînées
5. **Algorithmes avancés** comme la fusion de listes triées

## Concepts algorithmiques abordés

- **Structures de données linéaires**
- **Pointeurs et références**
- **Parcours de structures**
- **Algorithmes de tri et fusion**
- **Complexité temporelle et spatiale**

## Exécution

Pour tester l'exercice :

```bash
# Tester la correction
python correction_linked_list.py

# Ou travailler sur l'exercice
python ex_linked_list.py
```

## Sortie attendue

L'exécution de la correction produit une démonstration complète de toutes les fonctionnalités, incluant la gestion d'erreurs et l'affichage des concepts POO utilisés.

---

Cet exercice constitue une excellente synthèse des concepts de POO en Python et prépare les étudiants à comprendre des structures de données plus complexes.
