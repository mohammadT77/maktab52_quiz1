import pickle
from datetime import datetime, date

import dill as dill


class Book:
    ISBN: int
    name: str
    author: str
    publisher: str
    publish_date: datetime.date

    def __init__(self, ISBN, name, author, publisher, publish_date):
        self.ISBN = ISBN
        self.name = name
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date

    def __repr__(self):
        return f"<Book {self.ISBN}:{self.name} - {self.author},{self.publisher},{self.publish_date}>"


# books = [
#     Book(111111, 'Outliers', 'Malcolm Gladwell', 'Akbar pub', date(2001, 1, 1)),
#     Book(331111, '1984', 'George Orwell', 'Reza pub', date(1984, 1, 1)),
#     Book(735341, 'The Compound Effect', 'Darren Hardy', 'Reza pub', date(2006, 2, 5)),
#     Book(123456, 'Animal Farm', 'George Orwell', 'Akbar pub', date(2001, 6, 7)),
#     Book(654321, 'The Alchemist', 'Paulo Coelho', 'Akbar pub', date(1988, 1, 1)),
#     Book(122222, 'Eleven minutes', 'Paulo Coelho', 'Asqar pub', date(2010, 1, 1)),
#     Book(999999, 'The Pilgrimage', 'Paulo Coelho', 'Asqar pub', date(2019, 1, 1)),
# ]


with open('books.dill', 'rb') as f:
    books = dill.load(f)

# Or
with open('books.pkl', 'rb') as f:
    books = pickle.load(f)

s1 = sorted(books, key=lambda b: b.ISBN)
s2 = sorted(books, key=lambda b: b.name)
s3 = sorted(books, key=lambda b: b.publish_date, reverse=True)

f4 = filter(lambda b: b.author == "George Orwell", books)
f5 = filter(lambda b: b.publisher in ('Akbar pub', 'Asqar pub'), books)
f6 = filter(lambda b: b.publish_date.year >= 2001, books)

print(s1)
print(s2)
print(s3)
print(list(f4))
print(list(f5))
print(list(f6))

