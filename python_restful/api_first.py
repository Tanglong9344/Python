# A first restful api using flask
# reference: http://flask-restful.readthedocs.io/en/0.3.5/quickstart.html
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)  # set current file as a API


class First_API(Resource):
    def get(self):
        return {'message': 'first api data'}


api.add_resource(First_API, '/datas')  # add resources to a specific path '/datas'

if __name__ == '__main__':
        app.run(debug=True)

# We can get datas by visiting 'http://127.0.0.1:5000/datas'
# download curl: https://curl.haxx.se/download.html
# windows-64-zips
