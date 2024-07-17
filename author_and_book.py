class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info_book(self):
        print (f"Title: {self.title}, Author: {self.author.name}")
author=Author("Mark Twen","american")
book=Book("Tom Soyer",author)
book.get_info_book()
