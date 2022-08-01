import csv
from source.models.book import Book


def load_books():
    books = []
    with open('source/db/book.csv', 'r') as book_files:
        rows = csv.DictReader(book_files)
        for row in rows:
            books.append(Book(
                row['ISBN'],
                row['title'],
                row['author'],
                row['price'],
                row['published'],
                row['language'],
                row['number_pages'],
                row['press'],
                row['ranking']
            ))
        return books


def save_purchase_order(purchase):
    with open('src/db/purchase_order.csv', 'a') as purchase_file:
        # de esta forma se va a generar un nuevo archivo y lo que le vaya agregando no va a sobre escribir
        header = ['purchase_date', 'ISBN', 'user_id', 'full_address']

        writer = csv.DictWriter(purchase_file, fieldnames=header)

        if purchase_file.tell() == 0:
            writer.writeheader()

        writer.writerow(purchase)
