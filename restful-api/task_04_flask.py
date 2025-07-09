from flask import Flask, jsonify, request
import json

app = Flask(__name__)


users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return ("Welcome to Flask API!")

@app.route('/data')
def data():
    users_keys = list(users.keys())
    # print(users_keys)
    # print(users.keys())
    return jsonify(users_keys)

@app.route('/status')
def status():
    return ("OK")

@app.route('/users/<username>') #this is the input to check "username"
def get_user(username):
    user = users.get(username)
    if user:
        return (jsonify(user))
    else:
        return ({"error": "User not found"}, 404)

@app.route("/add_user", methods=["POST"]) #signifies the POST request
def add_data():
    user_data = request.get_json() #gets the json data that is input from client
    user_id = user_data.get("username") #reads the user_data and gets "username"s

    if not user_id:
        return (jsonify({"error": "Username is required"}), 400)

    users[user_id] = user_data #saves the "user_data" under the specific "user_id"

    return (jsonify({"message": "User added", "user": user_data}), 201)

if __name__ == "__main__": app.run()