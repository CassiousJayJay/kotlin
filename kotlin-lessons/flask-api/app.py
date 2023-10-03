from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "John De"},
    {"id": 3, "name": "Jon Do"},
    {"id": 4, "name": "Joh Doe"},
    {"id": 5, "name": "John Doe"},
    {"id": 6, "name": "John De"},
    {"id": 7, "name": "Jon Doe"},
]

@app.route("/api/users/", methods=['GET'])
def get_all():
    return jsonify(users)
    
@app.route("/api/users/<int:user_id>", methods=['GET'])
def get_one(user_id):
    user = next((user for user in users if user["id"] == user_id), None)    
    if user:
        return jsonify(user)
    else:
        return jsonify({"Error": "User not found"}), 404

@app.route("/api/create/", methods=["POST"])
def create_user():
    new_user = request.get_json()
    new_user_id = max(user["id"] for user in users) + 1
    new_user["id"] = new_user_id
    users.append(new_user)

    return jsonify(new_user), 201

@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    updated_user = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_user.get("name", user["name"])
            return jsonify(user), 200
        return jsonify({"error": "User found not"})
    
@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
   for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"Message": "User deleted"}), 200
        return jsonify({"error": "User found not"}), 404
   
if __name__ == "__main__":
    app.run(debug=True)