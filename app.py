from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
CORS(app, resources={r"/hello": {"origins": "http://localhost:3000"}})

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)
