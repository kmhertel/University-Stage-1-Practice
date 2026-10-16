#Library

class library_bookshelf:
    def __init__(self):
        self._bookshelf = []

    def check_book(self, pages):
        return pages >= 50

    def add_to_bookshelf(self, book, pages):
        if self.check_book(pages):
            self._bookshelf.append(book)

my_library_bookshelf = library_bookshelf()

addBook = input("Are you adding a book to the library? (Y/N) ")
if addBook == "Y":
    book = input("What book are you adding to the library? ")
    pages = int(input("How many pages are in the book? "))
    my_library_bookshelf.add_to_bookshelf(book, pages)

else:
    print("Thank you, goodbye")

#checks
print(my_library_bookshelf.check_book(pages))
print(my_library_bookshelf._bookshelf)
