from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')