from flask import Flask, jsonify, request
from flask_cors import CORS

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
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
