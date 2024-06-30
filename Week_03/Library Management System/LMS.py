class Book:
    def __init__(self, title, author, pages):
        # Initialize the Book class with title, author, and pages attributes
        self._title = title #here i used the _ sign to before my instence attributes to make them private or to encapsulate them
        self._author = author
        self._pages = pages

    # Getter methods
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_pages(self):
        return self._pages

    # Setter methods
    def set_title(self, new_title):
        self._title = new_title

    def set_author(self, new_author):
        self._author = new_author

    def set_pages(self, new_pages):
        self._pages = new_pages

    # Calculate the reading time based on an assumed reading speed
    def reading_time(self, words_per_page=250, words_per_minute=250):
        try:
            total_words = self._pages * words_per_page
            reading_time = total_words / words_per_minute
            return reading_time
        except TypeError:
            print("Error: Pages should be a number.")
            return None

class Ebook(Book):
    def __init__(self, title, author, pages, format):
        # Initialize the Ebook class, inheriting from Book and adding format attribute
        super().__init__(title, author, pages)
        self._format = format

    # Override the __str__() method to display all attributes
    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}, Format: {self._format}"

# Create an instance of Book and demonstrate the use of getter and setter methods
book1 = Book("Alchemist", "Paulo Coelho", 250)
print(f"Title: {book1.get_title()}, Author: {book1.get_author()}, Pages: {book1.get_pages()}")

# Update book details using setter methods
book1.set_title("Think and Grow Rich")
book1.set_author("Napoleon Hill")
book1.set_pages(300)
print(f"Title: {book1.get_title()}, Author: {book1.get_author()}, Pages: {book1.get_pages()}")

# Calculate the reading time for book1
reading_time = book1.reading_time()
if reading_time is not None:
    print(f"Reading time: {reading_time:.2f} minutes")

# Create an instance of Ebook
ebook1 = Ebook("Rich Dad Poor Dad", "Robert Kiyosaki", 350, "pdf")
print(ebook1)
