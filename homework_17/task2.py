"""Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book
class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods."""


class Author:
    author_total_numbers = 0

    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
        Author.author_total_numbers += 1

    def __str__(self):
        return f'Full name: {self.name}. \n' \
               f'Country: {self.country}. \n' \
               f'Birthday: {self.birthday}. \n' \
               f'Books: {self.books}.\n'

    def __repr__(self):
        return self.__str__()


class Book(Author):
    book_total_numbers = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.book_total_numbers += 1

    def __str__(self):
        return f'Book name: «{self.name}». \n' \
               f'Year: {self.year}. \n' \
               f'Author: {self.author.name} / {self.author.country} / {self.author.birthday}.\n'

    def __repr__(self):
        return self.__str__()


class Library(Book):
    def __init__(self, name):
        self.name = name
        self.all_books = []

    def new_book(self, book):
        if str(book.year).isdigit():
            pass
        else:
            self.all_books.append({'name': book.name, 'year': book.year, 'author': book.author.name})

    def group_by_author(self, author):
        book_count = 0
        print(f'All «{author.name}» books: ')
        for book in self.all_books:
            if author.name == book['author']:
                book_count += 1
                print(f"№{book_count}: «{book['name']}» ({book['year']} year)")
        print()
        if book_count == 0:
            print(f'Books «{author.name}» {self.name} not found.\n')

    def group_by_year(self, year):
        book_count = 0
        print(f'All {year} year books: ')
        for book in self.all_books:
            if year == book['year']:
                book_count += 1
                print(f"№{book_count}: «{book['name']}», author— {book['author']}")
        print()
        if book_count == 0:
            print(f'{self.name} does not have books {year} year.\n')

    def __str__(self):
        return f'Welcome to {self.name}! \n' \
               f'We have {Book.book_total_numbers} books.\n' \
               f'By {Author.author_total_numbers} authors.\n'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    our_library = Library('Library')
    author_1 = Author('Serhiy Zhadan', 'Ukraine', '23.08.1974', [])
    author_2 = Author('Yuval Noah Harari', 'Israel', '24.02.1976', [])
    book_1 = Book('Месопотамія', '2014', author_1)
    book_2 = Book('Тамплієри', '2016', author_1)
    book_3 = Book('Sapiens: A Brief History of Humankind', '2014', author_2)
    book_4 = Book('Homo Deus: A Brief History of Tomorrow ', '2016', author_2)
    our_library.new_book(book_1)
    our_library.new_book(book_2)
    our_library.new_book(book_3)
    our_library.new_book(book_4)
    our_library.group_by_author(author_1)
    our_library.group_by_author(author_2)
    our_library.group_by_year('2014')
    our_library.group_by_year('2016')
    print(our_library.__str__())