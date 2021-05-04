import dotenv

from flask import Flask, jsonify
from flask_cors import CORS


# configuration
dotenv.load_dotenv()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# BooksDB
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# books route
@app.route('/books', methods=['GET'])
def books():
    return {
        'status': 'success',
        'books': BOOKS
    }


if __name__ == '__main__':
    app.run()