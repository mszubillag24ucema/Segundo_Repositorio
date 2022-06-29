import csv


def load_books():
    books = []
    with open('source/db/book.csv', 'r') as book_files:

        rows = csv.DictReader(book_files)
        for row in rows:
            print(row)
        return
