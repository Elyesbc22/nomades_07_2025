# Exercice: Liste Chaînée avec POO
# 
# Dans cet exercice, vous allez créer une implémentation complète d'une liste chaînée
# en utilisant les concepts de POO vus en cours : classes, encapsulation, méthodes spéciales,
# propriétés, héritage et polymorphisme.

class Node:
    """
    Classe représentant un nœud dans une liste chaînée
    """
    
    def __init__(self, data):
        """
        Constructeur du nœud
        
        Args:
            data: Données stockées dans le nœud
        """
        # TODO: Initialisez les attributs privés __data et __next
        # __data contient les données du nœud
        # __next pointe vers le nœud suivant (None par défaut)
        pass
    
    @property
    def data(self):
        """Getter pour les données"""
        # TODO: Retournez __data
        pass
    
    @data.setter
    def data(self, value):
        """Setter pour les données"""
        # TODO: Assignez value à __data
        pass
    
    @property
    def next(self):
        """Getter pour le nœud suivant"""
        # TODO: Retournez __next
        pass
    
    @next.setter
    def next(self, node):
        """
        Setter pour le nœud suivant avec validation
        
        Args:
            node: Doit être un Node ou None
        """
        # TODO: Vérifiez que node est un Node ou None
        # Assignez à __next
        pass
    
    def __str__(self):
        """Représentation string du nœud"""
        # TODO: Retournez une représentation comme "Node(data)"
        pass
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return self.__str__()

class LinkedList:
    """
    Classe représentant une liste chaînée
    """
    
    def __init__(self):
        """Constructeur de la liste chaînée"""
        # TODO: Initialisez __head à None et __size à 0
        pass
    
    @property
    def size(self):
        """Propriété en lecture seule pour la taille"""
        # TODO: Retournez __size
        pass
    
    @property
    def is_empty(self):
        """Propriété calculée : vérifie si la liste est vide"""
        # TODO: Retournez True si __size == 0
        pass
    
    def __len__(self):
        """Surcharge de len() pour la liste"""
        # TODO: Retournez la taille de la liste
        pass
    
    def __str__(self):
        """
        Représentation string de la liste
        Format: [data1 -> data2 -> data3 -> None]
        """
        # TODO: Parcourez la liste et créez une représentation string
        # Si la liste est vide, retournez "[]"
        pass
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return f"LinkedList({self.__str__()})"
    
    def __iter__(self):
        """
        Rend la liste itérable
        Permet d'utiliser for item in linked_list
        """
        # TODO: Parcourez la liste en commençant par __head
        # Utilisez yield pour chaque élément de données
        pass
    
    def __getitem__(self, index):
        """
        Surcharge de l'opérateur [] pour l'accès par index
        
        Args:
            index (int): Index de l'élément
            
        Returns:
            Données à l'index donné
        """
        # TODO: Vérifiez que l'index est valide
        # Parcourez la liste jusqu'à l'index et retournez les données
        pass
    
    def __setitem__(self, index, value):
        """
        Surcharge de l'opérateur [] pour la modification par index
        
        Args:
            index (int): Index de l'élément
            value: Nouvelle valeur
        """
        # TODO: Vérifiez que l'index est valide
        # Parcourez la liste jusqu'à l'index et modifiez les données
        pass
    
    def __contains__(self, item):
        """
        Surcharge de l'opérateur 'in'
        
        Args:
            item: Élément à rechercher
            
        Returns:
            bool: True si l'élément est dans la liste
        """
        # TODO: Parcourez la liste et vérifiez si item est présent
        pass
    
    def __eq__(self, other):
        """
        Surcharge de l'opérateur == pour comparer deux listes
        
        Args:
            other (LinkedList): Autre liste chaînée
            
        Returns:
            bool: True si les listes sont égales
        """
        # TODO: Vérifiez que other est une LinkedList
        # Comparez la taille puis parcourez et comparez chaque élément
        pass
    
    def append(self, data):
        """
        Ajoute un élément à la fin de la liste
        
        Args:
            data: Données à ajouter
        """
        # TODO: Créez un nouveau nœud
        # Si la liste est vide, le nouveau nœud devient __head
        # Sinon, parcourez jusqu'à la fin et ajoutez le nœud
        # Incrémentez __size
        pass
    
    def prepend(self, data):
        """
        Ajoute un élément au début de la liste
        
        Args:
            data: Données à ajouter
        """
        # TODO: Créez un nouveau nœud
        # Le nouveau nœud pointe vers l'ancien __head
        # Le nouveau nœud devient __head
        # Incrémentez __size
        pass
    
    def insert(self, index, data):
        """
        Insère un élément à un index donné
        
        Args:
            index (int): Position d'insertion
            data: Données à insérer
        """
        # TODO: Vérifiez que l'index est valide (0 <= index <= size)
        # Si index == 0, utilisez prepend
        # Si index == size, utilisez append
        # Sinon, parcourez jusqu'à index-1 et insérez le nouveau nœud
        pass
    
    def remove(self, data):
        """
        Supprime la première occurrence d'un élément
        
        Args:
            data: Données à supprimer
            
        Returns:
            bool: True si l'élément a été supprimé
        """
        # TODO: Si la liste est vide, retournez False
        # Si __head contient data, supprimez __head
        # Sinon, parcourez et trouvez le nœud précédent celui à supprimer
        # Reconnectez les nœuds et décrémentez __size
        pass
    
    def remove_at(self, index):
        """
        Supprime l'élément à un index donné
        
        Args:
            index (int): Index de l'élément à supprimer
            
        Returns:
            Données supprimées
        """
        # TODO: Vérifiez que l'index est valide
        # Si index == 0, supprimez __head
        # Sinon, parcourez jusqu'à index-1 et supprimez le nœud suivant
        # Décrémentez __size et retournez les données supprimées
        pass
    
    def find(self, data):
        """
        Trouve l'index de la première occurrence d'un élément
        
        Args:
            data: Données à rechercher
            
        Returns:
            int: Index de l'élément (-1 si non trouvé)
        """
        # TODO: Parcourez la liste en gardant un compteur d'index
        # Retournez l'index si trouvé, -1 sinon
        pass
    
    def clear(self):
        """Vide la liste"""
        # TODO: Remettez __head à None et __size à 0
        pass
    
    def reverse(self):
        """Inverse l'ordre des éléments dans la liste"""
        # TODO: Parcourez la liste en inversant les liens
        # prev = None, current = __head
        # Pour chaque nœud: next_node = current.next, current.next = prev, prev = current, current = next_node
        # À la fin: __head = prev
        pass
    
    @staticmethod
    def merge_sorted(list1, list2):
        """
        Fusionne deux listes triées en une liste triée
        
        Args:
            list1 (LinkedList): Première liste triée
            list2 (LinkedList): Deuxième liste triée
            
        Returns:
            LinkedList: Nouvelle liste fusionnée et triée
        """
        # TODO: Créez une nouvelle liste résultat
        # Utilisez deux pointeurs pour parcourir list1 et list2
        # Comparez les éléments et ajoutez le plus petit au résultat
        # Ajoutez les éléments restants de la liste non épuisée
        pass

class DoublyNode(Node):
    """
    Classe représentant un nœud dans une liste doublement chaînée
    Hérite de Node et ajoute un lien vers le nœud précédent
    """
    
    def __init__(self, data):
        """Constructeur du nœud doublement chaîné"""
        # TODO: Appelez le constructeur parent
        # Initialisez __prev à None
        pass
    
    @property
    def prev(self):
        """Getter pour le nœud précédent"""
        # TODO: Retournez __prev
        pass
    
    @prev.setter
    def prev(self, node):
        """
        Setter pour le nœud précédent avec validation
        
        Args:
            node: Doit être un DoublyNode ou None
        """
        # TODO: Vérifiez que node est un DoublyNode ou None
        # Assignez à __prev
        pass

class DoublyLinkedList(LinkedList):
    """
    Liste doublement chaînée qui hérite de LinkedList
    Démontre l'héritage et la surcharge de méthodes
    """
    
    def __init__(self):
        """Constructeur de la liste doublement chaînée"""
        # TODO: Appelez le constructeur parent
        # Initialisez __tail à None
        pass
    
    @property
    def tail(self):
        """Getter pour le dernier nœud"""
        # TODO: Retournez __tail
        pass
    
    def append(self, data):
        """
        Surcharge de append pour liste doublement chaînée
        
        Args:
            data: Données à ajouter
        """
        # TODO: Créez un nouveau DoublyNode
        # Si la liste est vide, le nouveau nœud devient __head et __tail
        # Sinon, connectez le nouveau nœud après __tail et mettez à jour __tail
        # Incrémentez la taille
        pass
    
    def prepend(self, data):
        """
        Surcharge de prepend pour liste doublement chaînée
        
        Args:
            data: Données à ajouter
        """
        # TODO: Créez un nouveau DoublyNode
        # Si la liste est vide, le nouveau nœud devient __head et __tail
        # Sinon, connectez le nouveau nœud avant __head et mettez à jour __head
        # Incrémentez la taille
        pass
    
    def reverse_iterate(self):
        """
        Générateur pour itérer en sens inverse
        
        Yields:
            Données des nœuds en ordre inverse
        """
        # TODO: Commencez par __tail et parcourez vers __head
        # Utilisez yield pour chaque élément de données
        pass

# Tests et démonstrations
if __name__ == "__main__":
    print("=== Test de la classe Node ===")
    node1 = Node("A")
    node2 = Node("B")
    node1.next = node2
    print(f"Node 1: {node1}")
    print(f"Node 1 next: {node1.next}")
    
    print("\n=== Test de la classe LinkedList ===")
    
    # Test de création et ajout
    ll = LinkedList()
    print(f"Liste vide: {ll}")
    print(f"Taille: {len(ll)}")
    print(f"Est vide: {ll.is_empty}")
    
    # Test d'ajout
    ll.append("Premier")
    ll.append("Deuxième")
    ll.prepend("Début")
    print(f"Après ajouts: {ll}")
    print(f"Taille: {len(ll)}")
    
    # Test d'insertion
    ll.insert(1, "Inséré")
    print(f"Après insertion: {ll}")
    
    # Test d'accès par index
    print(f"Élément à l'index 0: {ll[0]}")
    print(f"Élément à l'index 2: {ll[2]}")
    
    # Test de modification
    ll[1] = "Modifié"
    print(f"Après modification: {ll}")
    
    # Test de recherche
    print(f"'Premier' dans la liste: {'Premier' in ll}")
    print(f"Index de 'Deuxième': {ll.find('Deuxième')}")
    
    # Test d'itération
    print("Itération sur la liste:")
    for item in ll:
        print(f"  - {item}")
    
    # Test de suppression
    ll.remove("Début")
    print(f"Après suppression de 'Début': {ll}")
    
    supprimé = ll.remove_at(0)
    print(f"Élément supprimé à l'index 0: {supprimé}")
    print(f"Liste après suppression: {ll}")
    
    # Test d'inversion
    ll.append("Fin")
    print(f"Avant inversion: {ll}")
    ll.reverse()
    print(f"Après inversion: {ll}")
    
    # Test d'égalité
    ll2 = LinkedList()
    ll2.append("Fin")
    ll2.append("Deuxième")
    ll2.append("Premier")
    print(f"Liste 1: {ll}")
    print(f"Liste 2: {ll2}")
    print(f"Les listes sont égales: {ll == ll2}")
    
    print("\n=== Test de fusion de listes triées ===")
    list1 = LinkedList()
    list2 = LinkedList()
    
    # Créer deux listes triées
    for i in [1, 3, 5]:
        list1.append(i)
    for i in [2, 4, 6]:
        list2.append(i)
    
    print(f"Liste 1 triée: {list1}")
    print(f"Liste 2 triée: {list2}")
    
    merged = LinkedList.merge_sorted(list1, list2)
    print(f"Liste fusionnée: {merged}")
    
    print("\n=== Test de la liste doublement chaînée ===")
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.prepend("Début")
    print(f"Liste doublement chaînée: {dll}")
    
    print("Itération normale:")
    for item in dll:
        print(f"  - {item}")
    
    print("Itération inverse:")
    for item in dll.reverse_iterate():
        print(f"  - {item}")
    
    print("\n=== Démonstration des concepts POO utilisés ===")
    print("✓ Classes et objets: Node, LinkedList, DoublyNode, DoublyLinkedList")
    print("✓ Encapsulation: Attributs privés (__data, __next, __head, __size)")
    print("✓ Propriétés: @property pour data, next, size, is_empty")
    print("✓ Méthodes spéciales: __str__, __len__, __iter__, __getitem__, __setitem__, __contains__, __eq__")
    print("✓ Héritage: DoublyNode hérite de Node, DoublyLinkedList hérite de LinkedList")
    print("✓ Surcharge de méthodes: append() et prepend() redéfinies dans DoublyLinkedList")
    print("✓ Méthodes statiques: merge_sorted() utilise @staticmethod")
    print("✓ Polymorphisme: Les deux types de listes peuvent être utilisées de manière similaire")
