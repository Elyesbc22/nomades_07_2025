# Exercice POO - Système de Gestion de Bibliothèque

## Partie 1: Création de la classe Book

# Créez une classe `Book` qui représente un livre dans une bibliothèque.

class Book:
    def __init__(self, title, author, isbn, pages):
        """
        Constructeur de la classe Book
        - title: titre du livre (str)
        - author: auteur du livre (str) 
        - isbn: numéro ISBN (str)
        - pages: nombre de pages (int)
        """
        # TODO: Initialisez les attributs
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__pages = pages
    
    def __str__(self):
        """Retourne une représentation lisible du livre"""
        return f"{self.__title}, {self.__author}"
    
    def __eq__(self, other):
        """Compare deux livres par leur ISBN"""
        return self.__isbn == other.__isbn
    
    def is_long_book(self):
        """Retourne True si le livre a plus de 300 pages"""
        return self.__pages > 300
    
    def get_isbn(self):
        return self.__isbn
    
    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

## Partie 2: Héritage - Types de livres spécialisés

class Fiction(Book):
    def __init__(self, title, author, isbn, pages, genre):
        """
        Classe pour les livres de fiction
        - genre: genre de fiction (str)
        """
        Book.__init__(self, title, author, isbn, pages)
        self.__genre = genre
    
    def __str__(self):
        """Override pour inclure le genre"""
        # TODO: Utilisez super() et ajoutez le genre
        return f"{super().__str__()}, {self.__genre}"

class NonFiction(Book):
    def __init__(self, title, author, isbn, pages, subject):
        """
        Classe pour les livres de fiction
        - genre: genre de fiction (str)
        """
        Book.__init__(self, title, author, isbn, pages)
        self.subject = subject
    
    def __str__(self):
        """Override pour inclure le genre"""
        # TODO: Utilisez super() et ajoutez le genre
        return f"{super().__str__()}, {self.subject}"

## Partie 3: Classe Library avec encapsulation

class Library:
    def __init__(self, name):
        """
        Constructeur de la bibliothèque
        - name: nom de la bibliothèque (str)
        """
        self.name = name
        self.__books = []  # Liste privée des livres
        self.__total_books = 0  # Compteur privé
    
    def add_book(self, book):
        """Ajoute un livre à la bibliothèque"""
        self.__books.append(book)
    
    def remove_book(self, isbn):
        """Supprime un livre par son ISBN"""
        for book in self.__books:
            if book.get_isbn() == isbn:
                self.__books.remove(book)
            
    def find_book_by_author(self, author):
        """Trouve tous les livres d'un auteur"""
        books = []
        for book in self.__books:
            if book.get_author() == author:
                books.append(book)
        return books
    
    def get_total_books(self):
        """Getter pour le nombre total de livres"""
        self.__total_books = len(self.__books)
        return self.__total_books
            
    def get_books(self):
        """Getter pour la liste des livres (copie)"""
        return self.__books
    
    def __str__(self):
        """Représentation de la bibliothèque"""
        return f"{self.name}"
    
    @property
    def average_pages(self):
        """Propriété calculée: moyenne des pages des livres"""
        avg_pages = 0
        sum = 0
        for book in self.__books:
            pages = book.get_pages()
            sum = sum + pages
            
        avg_pages = sum / self.__total_books
        return avg_pages
        
## Partie 4: Tests de votre implémentation

# Testez votre code ici
if __name__ == "__main__":
    # Créer des livres
    book1 = Fiction("1984", "George Orwell", "978-0451524935", 328, "Dystopie")
    book2 = NonFiction("Sapiens", "Yuval Noah Harari", "978-0062316097", 443, "Histoire")
    book3 = Fiction("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070408504", 96, "Conte")
    
    # Créer une bibliothèque
    ma_bibliotheque = Library("Bibliothèque Nomades")
    
    # Ajouter des livres
    ma_bibliotheque.add_book(book1)
    ma_bibliotheque.add_book(book2)
    ma_bibliotheque.add_book(book3)
    
    # Tests
    print(ma_bibliotheque)
    print(f"Nombre total de livres: {ma_bibliotheque.get_total_books()}")
    print(f"Moyenne des pages: {ma_bibliotheque.average_pages:.1f}")
    
    print("\nLivres de fiction longue (>300 pages):")
    for book in ma_bibliotheque.get_books():
        if isinstance(book, Fiction) and book.is_long_book():
            print(f"- {book}")
    
    print(f"\nLivres de George Orwell:")
    orwell_books = ma_bibliotheque.find_book_by_author("George Orwell")
    for book in orwell_books:
        print(f"- {book}")

## Bonus: Operator Overloading

class BookCollection:
    """Classe pour gérer une collection de livres avec des opérateurs"""
    
    def __init__(self, books=None):
        self.books = books or []
    
    def __add__(self, other):
        """Combine deux collections de livres"""
        # TODO: Retournez une nouvelle collection avec tous les livres
        pass
    
    def __len__(self):
        """Retourne le nombre de livres dans la collection"""
        # TODO: Retournez la longueur de la liste
        pass
    
    def __contains__(self, book):
        """Vérifie si un livre est dans la collection"""
        # TODO: Vérifiez si le livre est présent
        pass

# Test du bonus
collection1 = BookCollection([book1, book2])
collection2 = BookCollection([book3])
collection_totale = collection1 + collection2

print(f"\nCollection totale: {len(collection_totale)} livres")
print(f"Le livre '1984' est dans la collection: {book1 in collection_totale}")