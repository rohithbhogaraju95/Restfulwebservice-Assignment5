import json
from flask import Flask, render_template, request, Response

app = Flask(__name__)

with open('books.json') as json_data:
    books_data = json.load(json_data)['books']

@app.route('/books', methods=['GET'])
def books():
    return render_template('books.html', list_data=books_data)

@app.route('/books/<string:book_id>', methods=['GET'])
def book_info(book_id):
    book = next((b for b in books_data if b['id'] == book_id), None)
    if book is None:
        return render_template('Error.html')
    else:
        return render_template('books.html', list_data=[book])

@app.route('/books/<book_id>/orders', methods=['GET'])
def sales(book_id):
    book = next((b for b in books_data if b['id'] == book_id), None)
    if book is None:
        return render_template('Error.html')
    else:
        sale_details = book['orders']
        return render_template('books.html', list_data=sale_details)

@app.route('/books/<book_id>/orders/<order_id>', methods=['GET'])
def sale_info(book_id, order_id):
    book = next((b for b in books_data if b['id'] == book_id), None)
    if book is None:
        return render_template('Error.html')
    else:
        order = next((s for s in book['orders'] if s['order_id'] == order_id), None)
        if order is None:
            return render_template('Error.html')
        else:
            return render_template('books.html', list_data=[order])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
