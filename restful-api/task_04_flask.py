from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store users
users = {}

# Welcome message
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# JSON response with list of all usernames
@app.route('/data')
def get_all_usernames():
    return jsonify(list(users.keys()))

# Status endpoint
@app.route('/status')
def status():
    return "OK"

# Get user by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Add new user
@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.json
    username = user_data.get('username')
    if username:
        users[username] = user_data
        return jsonify({
            "message": "User added",
            "user": user_data
        }), 201
    else:
        return jsonify({"error": "Username not provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
