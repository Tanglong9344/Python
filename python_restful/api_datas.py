# add one more resources
# reference: http://flask-restful.readthedocs.io/en/0.3.5/quickstart.html
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)  # set current file as a API


class Message1(Resource):
    def get(self):
        # Response code default to 200
        return {'message': 'data111'}


class Message2(Resource):
    def get(self):
        # Set response code to 201
        return {'message': 'data222'}, 201


class Message3(Resource):
    def get(self):
        # Set response code to 201 and return a custom header
        return {'message': 'data333'}, 201, {'header': 'A custom header'}


api.add_resource(Message1, '/data1')  # add resources to a specific path '/data1'
api.add_resource(Message2, '/data2')  # add resources to a specific path '/data2'
api.add_resource(Message3, '/data3')  # add resources to a specific path '/data3'

if __name__ == '__main__':
        app.run(debug=True)

# We can get datas by visiting 'http://127.0.0.1:5000/data(1|2|3)'
