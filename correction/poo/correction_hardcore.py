# Correction de l'exercice: Liste Chaînée avec POO
# 
# Implémentation complète d'une liste chaînée utilisant tous les concepts de POO

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
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        """Getter pour les données"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """Setter pour les données"""
        self.__data = value
    
    @property
    def next(self):
        """Getter pour le nœud suivant"""
        return self.__next
    
    @next.setter
    def next(self, node):
        """
        Setter pour le nœud suivant avec validation
        
        Args:
            node: Doit être un Node ou None
        """
        if node is not None and not isinstance(node, Node):
            raise TypeError("Le nœud suivant doit être un Node ou None")
        self.__next = node
    
    def __str__(self):
        """Représentation string du nœud"""
        return f"Node({self.__data})"
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return self.__str__()

class LinkedList:
    """
    Classe représentant une liste chaînée
    """
    
    def __init__(self):
        """Constructeur de la liste chaînée"""
        self.__head = None
        self.__size = 0
    
    @property
    def size(self):
        """Propriété en lecture seule pour la taille"""
        return self.__size
    
    @property
    def is_empty(self):
        """Propriété calculée : vérifie si la liste est vide"""
        return self.__size == 0
    
    def __len__(self):
        """Surcharge de len() pour la liste"""
        return self.__size
    
    def __str__(self):
        """
        Représentation string de la liste
        Format: [data1 -> data2 -> data3 -> None]
        """
        if self.is_empty:
            return "[]"
        
        result = "["
        current = self.__head
        while current is not None:
            result += str(current.data)
            current = current.next
            if current is not None:
                result += " -> "
        result += " -> None]"
        return result
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return f"LinkedList({self.__str__()})"
    
    def __iter__(self):
        """
        Rend la liste itérable
        Permet d'utiliser for item in linked_list
        """
        current = self.__head
        while current is not None:
            yield current.data
            current = current.next
    
    def __getitem__(self, index):
        """
        Surcharge de l'opérateur [] pour l'accès par index
        
        Args:
            index (int): Index de l'élément
            
        Returns:
            Données à l'index donné
        """
        if not isinstance(index, int):
            raise TypeError("L'index doit être un entier")
        if index < 0 or index >= self.__size:
            raise IndexError("Index hors limites")
        
        current = self.__head
        for _ in range(index):
            current = current.next
        return current.data
    
    def __setitem__(self, index, value):
        """
        Surcharge de l'opérateur [] pour la modification par index
        
        Args:
            index (int): Index de l'élément
            value: Nouvelle valeur
        """
        if not isinstance(index, int):
            raise TypeError("L'index doit être un entier")
        if index < 0 or index >= self.__size:
            raise IndexError("Index hors limites")
        
        current = self.__head
        for _ in range(index):
            current = current.next
        current.data = value
    
    def __contains__(self, item):
        """
        Surcharge de l'opérateur 'in'
        
        Args:
            item: Élément à rechercher
            
        Returns:
            bool: True si l'élément est dans la liste
        """
        current = self.__head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def __eq__(self, other):
        """
        Surcharge de l'opérateur == pour comparer deux listes
        
        Args:
            other (LinkedList): Autre liste chaînée
            
        Returns:
            bool: True si les listes sont égales
        """
        if not isinstance(other, LinkedList):
            return False
        
        if self.__size != other.__size:
            return False
        
        current1 = self.__head
        current2 = other.__head
        
        while current1 is not None:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
        
        return True
    
    def append(self, data):
        """
        Ajoute un élément à la fin de la liste
        
        Args:
            data: Données à ajouter
        """
        new_node = Node(data)
        
        if self.is_empty:
            self.__head = new_node
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = new_node
        
        self.__size += 1
    
    def prepend(self, data):
        """
        Ajoute un élément au début de la liste
        
        Args:
            data: Données à ajouter
        """
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1
    
    def insert(self, index, data):
        """
        Insère un élément à un index donné
        
        Args:
            index (int): Position d'insertion
            data: Données à insérer
        """
        if not isinstance(index, int):
            raise TypeError("L'index doit être un entier")
        if index < 0 or index > self.__size:
            raise IndexError("Index hors limites")
        
        if index == 0:
            self.prepend(data)
        elif index == self.__size:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.__head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.__size += 1
    
    def remove(self, data):
        """
        Supprime la première occurrence d'un élément
        
        Args:
            data: Données à supprimer
            
        Returns:
            bool: True si l'élément a été supprimé
        """
        if self.is_empty:
            return False
        
        if self.__head.data == data:
            self.__head = self.__head.next
            self.__size -= 1
            return True
        
        current = self.__head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.__size -= 1
                return True
            current = current.next
        
        return False
    
    def remove_at(self, index):
        """
        Supprime l'élément à un index donné
        
        Args:
            index (int): Index de l'élément à supprimer
            
        Returns:
            Données supprimées
        """
        if not isinstance(index, int):
            raise TypeError("L'index doit être un entier")
        if index < 0 or index >= self.__size:
            raise IndexError("Index hors limites")
        
        if index == 0:
            data = self.__head.data
            self.__head = self.__head.next
            self.__size -= 1
            return data
        
        current = self.__head
        for _ in range(index - 1):
            current = current.next
        
        data = current.next.data
        current.next = current.next.next
        self.__size -= 1
        return data
    
    def find(self, data):
        """
        Trouve l'index de la première occurrence d'un élément
        
        Args:
            data: Données à rechercher
            
        Returns:
            int: Index de l'élément (-1 si non trouvé)
        """
        current = self.__head
        index = 0
        
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def clear(self):
        """Vide la liste"""
        self.__head = None
        self.__size = 0
    
    def reverse(self):
        """Inverse l'ordre des éléments dans la liste"""
        prev = None
        current = self.__head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.__head = prev
    
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
        if not isinstance(list1, LinkedList) or not isinstance(list2, LinkedList):
            raise TypeError("Les deux arguments doivent être des LinkedList")
        
        result = LinkedList()
        current1 = list1.__head
        current2 = list2.__head
        
        while current1 is not None and current2 is not None:
            if current1.data <= current2.data:
                result.append(current1.data)
                current1 = current1.next
            else:
                result.append(current2.data)
                current2 = current2.next
        
        # Ajouter les éléments restants
        while current1 is not None:
            result.append(current1.data)
            current1 = current1.next
        
        while current2 is not None:
            result.append(current2.data)
            current2 = current2.next
        
        return result

class DoublyNode(Node):
    """
    Classe représentant un nœud dans une liste doublement chaînée
    Hérite de Node et ajoute un lien vers le nœud précédent
    """
    
    def __init__(self, data):
        """Constructeur du nœud doublement chaîné"""
        super().__init__(data)
        self.__prev = None
    
    @property
    def prev(self):
        """Getter pour le nœud précédent"""
        return self.__prev
    
    @prev.setter
    def prev(self, node):
        """
        Setter pour le nœud précédent avec validation
        
        Args:
            node: Doit être un DoublyNode ou None
        """
        if node is not None and not isinstance(node, DoublyNode):
            raise TypeError("Le nœud précédent doit être un DoublyNode ou None")
        self.__prev = node

class DoublyLinkedList(LinkedList):
    """
    Liste doublement chaînée qui hérite de LinkedList
    Démontre l'héritage et la surcharge de méthodes
    """
    
    def __init__(self):
        """Constructeur de la liste doublement chaînée"""
        super().__init__()
        self.__tail = None
    
    @property
    def tail(self):
        """Getter pour le dernier nœud"""
        return self.__tail
    
    def append(self, data):
        """
        Surcharge de append pour liste doublement chaînée
        
        Args:
            data: Données à ajouter
        """
        new_node = DoublyNode(data)
        
        if self.is_empty:
            self._LinkedList__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node
        
        self._LinkedList__size += 1
    
    def prepend(self, data):
        """
        Surcharge de prepend pour liste doublement chaînée
        
        Args:
            data: Données à ajouter
        """
        new_node = DoublyNode(data)
        
        if self.is_empty:
            self._LinkedList__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self._LinkedList__head
            self._LinkedList__head.prev = new_node
            self._LinkedList__head = new_node
        
        self._LinkedList__size += 1
    
    def reverse_iterate(self):
        """
        Générateur pour itérer en sens inverse
        
        Yields:
            Données des nœuds en ordre inverse
        """
        current = self.__tail
        while current is not None:
            yield current.data
            current = current.prev

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
    
    print("\n=== Test de gestion d'erreurs ===")
    try:
        print(ll[100])  # Index hors limites
    except IndexError as e:
        print(f"Erreur capturée: {e}")
    
    try:
        node1.next = "pas un nœud"  # Type incorrect
    except TypeError as e:
        print(f"Erreur capturée: {e}")
    
    print("\n=== Démonstration des concepts POO utilisés ===")
    print("✓ Classes et objets: Node, LinkedList, DoublyNode, DoublyLinkedList")
    print("✓ Encapsulation: Attributs privés (__data, __next, __head, __size)")
    print("✓ Propriétés: @property pour data, next, size, is_empty")
    print("✓ Méthodes spéciales: __str__, __len__, __iter__, __getitem__, __setitem__, __contains__, __eq__")
    print("✓ Héritage: DoublyNode hérite de Node, DoublyLinkedList hérite de LinkedList")
    print("✓ Surcharge de méthodes: append() et prepend() redéfinies dans DoublyLinkedList")
    print("✓ Méthodes statiques: merge_sorted() utilise @staticmethod")
    print("✓ Polymorphisme: Les deux types de listes peuvent être utilisées de manière similaire")
    print("✓ Gestion d'exceptions: Validation des types et des indices")
