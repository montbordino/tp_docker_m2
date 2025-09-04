from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connexion MongoDB (le hostname sera "mongo" = nom du service docker-compose)
client = MongoClient("mongodb://mongo:27017/")

# On sélectionne une base et une collection
db = client["testdb"]
collection = db["messages"]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/mongo-test")
def mongo_test():
    collection.insert_one({"message": "Connexion réussie avec MongoDB"})
    last_message = collection.find().sort("_id", -1).limit(1)[0]
    return jsonify({"mongo_message": last_message["message"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
