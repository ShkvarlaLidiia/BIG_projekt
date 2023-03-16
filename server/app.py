from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from utils.toJSON import toJSON
from model.User.User import User
from model.Product.Product import Product
from connection import connection

users = toJSON([
    User("k@.ua", "John", "2323")
])


app = Flask(__name__)
CORS(app)


def getData(arr):
    return arr

# @app.route("/")
# def home():
#     return "<h2>Server works!</h2>"

@app.route("/products")
def products():
    print(request.method)
    return jsonify(toJSON([
    Product(
        "Bitcoin", 
        "$21453.78", 
        "https://static.vecteezy.com/system/resources/previews/008/822/064/original/3d-design-bitcoin-cryptocurrency-white-background-free-png.png", 
        "Bitcoin (BTC) is a form of digital money. It exists on its own network that facilitates secure, online transactions directly between accounts without requiring an intermediary — such as a bank or credit card company — to mediate and validate transactions."
    ),
    Product(
        "Ethereum", 
        "$1526.76",
        "https://w7.pngwing.com/pngs/268/1013/png-transparent-ethereum-eth-hd-logo-thumbnail.png", 
        "Bitcoin (BTC) is a form of digital money. It exists on its own network that facilitates secure, online transactions directly between accounts without requiring an intermediary — such as a bank or credit card company — to mediate and validate transactions."
    ),
    Product(
        "Tether", 
        "$0.9999", 
        "https://w7.pngwing.com/pngs/917/678/png-transparent-tether-tether-coin-cryptocurrency-logo-bitcoin-crypto-currency-cryptocurrency-sign-3d-icon-thumbnail.png", 
        "Bitcoin (BTC) is a form of digital money. It exists on its own network that facilitates secure, online transactions directly between accounts without requiring an intermediary — such as a bank or credit card company — to mediate and validate transactions."
    ),
    Product(
        "BNB", 
        "$287.40", 
        "https://w7.pngwing.com/pngs/1007/775/png-transparent-bnb-cryptocurrencies-icon-thumbnail.png", 
        "Bitcoin (BTC) is a form of digital money. It exists on its own network that facilitates secure, online transactions directly between accounts without requiring an intermediary — such as a bank or credit card company — to mediate and validate transactions."
    ),
    Product(
        "Dogecoin", 
        "0.07125", 
        "https://w7.pngwing.com/pngs/191/349/png-transparent-dogecoin-bitcoin-cryptocurrency-exchange-bitcoin-dog-like-mammal-meme-bitcoin.png", 
        "Bitcoin (BTC) is a form of digital money. It exists on its own network that facilitates secure, online transactions directly between accounts without requiring an intermediary — such as a bank or credit card company — to mediate and validate transactions."
    ),
    Product(
        "Solana", 
        "18.12", 
        "https://www.pngall.com/wp-content/uploads/10/Solana-Crypto-Logo-PNG-File.png", 
        "Bitcoin (BTC) is a form of digital money. It exists on its own network that facilitates secure, online transactions directly between accounts without requiring an intermediary — such as a bank or credit card company — to mediate and validate transactions."
    )
    ]))

# class Song:
#     def __init__(self, title, artist, year):
#         self.title = title
#         self.artist = artist
#         self.year = year
    
# songs = [
#     Song("Sweet Child o' Mine", "Guns N' Roses", 1987),
#     Song("Imagine", "John Lennon", 1971),
#     Song("Thriller", "Michael Jackson", 1982)
# ]

# @app.route('/playlist')
# def playlist():
#     return jsonify(toJSON(songs))





# @app.route("/products")
# def products():
#     try :
#         return json.dumps(products)
#     except :
#         print("Error handled")


# @app.route("/products")
# def users():
#     return

treck = {
    "author" : "John Lennon",
    "name" : "Imagine", 
    "year" : "1971"
}

def get_data():
    data = connection()
    data_collection = data['music']
    
    return data_collection.find()

@app.route("/")
def home():
    data = get_data()    
    # music = [doc for doc in data]
    music = []
    
    for doc in data:
        doc ['_id'] = str(doc['_id'])
        print(doc)
        music.append(doc)
    return {        
        "music" : music
    }
      
if __name__ == "__main__":
    app.run()


    # User("m@.ua", "Mike", "1241"),
    # User("b@i.ua", "Bob", "1242"),
    # User("d@i.ua", "Doe", "42112")
    