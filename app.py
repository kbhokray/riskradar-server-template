from flask import Flask, jsonify, request
from flask_cors import CORS
from service import predict_one, get_user_details, get_all_users, predict

"""
Create a flask app with the following end points:
    GET /
    GET /users
    GET /users/<int:user_id>
    GET /testpredict
    GET /users/<int:user_id>/prediction
"""

app = Flask(__name__)

CORS(app=app, supports_credentials=True)


@app.route("/")
def hello_world():
    return "Hey World!"


@app.route("/testpredict")
def predict_testing():
    result = predict_one()
    return jsonify(result)


@app.route("/users/<int:user_id>")
def get_userdetails(user_id):
    result = get_user_details(user_id)
    return jsonify(result)


@app.route("/users")
def get_allusers():
    result = get_all_users()
    return jsonify(result)


@app.route("/users/<int:user_id>/prediction")
def predict_(user_id):
    result = predict(user_id)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
