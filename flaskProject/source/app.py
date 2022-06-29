from flask import Flask, jsonify
from db.db_manager import load_books
app = Flask(__name__)
books = load_books()


@app.route('/academic-books/books', methods=['GET'])
def get_books():
    return jsonify([book.serialize() for book in books])


if __name__ == '__main__':
    app.run()
