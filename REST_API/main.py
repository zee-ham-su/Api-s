from flask import Flask, requests, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
BASE= 'http://127.0.0.1:5000/'
response = requests.get(BASE + 'helloworld')
print(response.json())


class HelloWorld(Resource):
    def get(self):
        return {"data": 'hello world'}

api.add_resource(HelloWorld, '/helloworld')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')