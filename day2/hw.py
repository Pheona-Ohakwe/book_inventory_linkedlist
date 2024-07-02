# Lesson 3: Assignment | Linked List
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

# Implementing a BookInventory Linked List in Python
# Objective: The aim of this assignment is to reinforce understanding of the linked list data structure and its implementation in Python.

# Problem Statement: You are tasked with building an inventory management system for a bookstore. The system should allow adding new books to the inventory and removing books based on their ISBN. You'll implement this system using a linked list data structure.

# Task 1

# Create a class named Book with attributes for title, author, genre, ISBN, and quantity.

class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ISBN: {self.isbn}, Quantity: {self.quantity}"

# Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", "9780743273565", 10)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "9780061120084", 5)

print(book1)
print(book2)

# Task 2

# Create a class named Node to represent nodes in the linked list. Each node will store a book object.

class Node:
    def __init__(self, book=None, next=None):
        self.book = book  # Store the Book object
        self.next = next  # Reference to the next Node
    
    def __str__(self):
        return str(self.book)  # Return the string representation of the Book object

# Example usage:
# Assuming the Book class from the previous example is defined...

# Create some Book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", "9780743273565", 10)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "9780061120084", 5)

# Create nodes with these Book objects
node1 = Node(book1)
node2 = Node(book2)

# Link the nodes manually
node1.next = node2

# Printing the nodes will call the __str__ method of Node, which in turn calls __str__ of Book
print(node1)
print(node2)

# Task 3

# Implement a class named InventoryManager to manage the inventory using a linked list.
class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ISBN: {self.isbn}, Quantity: {self.quantity}"

class Node:
    def __init__(self, book=None, next=None):
        self.book = book
        self.next = next
    
    def __str__(self):
        return str(self.book)

class InventoryManager:
    def __init__(self):
        self.head = None  # Initialize an empty linked list
    
    def add_book(self, book):
        new_node = Node(book)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def remove_book(self, isbn):
        current = self.head
        prev = None
        while current:
            if current.book.isbn == isbn:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return  # Exit after removing the node
            prev = current
            current = current.next
        print(f"Book with ISBN {isbn} not found.")
    
    def display_inventory(self):
        current = self.head
        while current:
            print(current)
            current = current.next
        print("End of Inventory")

# Task 4

# Implement the following methods in the **`InventoryManager`** class:
# add_book(title, author, genre, isbn, quantity): Adds a new book to the inventory.
# remove_book(isbn): Removes a book from the inventory based on its ISBN.
# display_inventory(): Displays the current inventory.

class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ISBN: {self.isbn}, Quantity: {self.quantity}"

class Node:
    def __init__(self, book=None, next=None):
        self.book = book
        self.next = next
    
    def __str__(self):
        return str(self.book)

class InventoryManager:
    def __init__(self):
        self.head = None  # Initialize an empty linked list
    
    def add_book(self, title, author, genre, isbn, quantity):
        new_book = Book(title, author, genre, isbn, quantity)
        new_node = Node(new_book)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def remove_book(self, isbn):
        current = self.head
        prev = None
        while current:
            if current.book.isbn == isbn:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return  # Exit after removing the node
            prev = current
            current = current.next
        print(f"Book with ISBN {isbn} not found.")
    
    def display_inventory(self):
        if not self.head:
            print("Inventory is empty.")
        else:
            current = self.head
            while current:
                print(current)
                current = current.next
            print("End of Inventory")

