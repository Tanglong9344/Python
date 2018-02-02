# some methods(crud) on resources
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

datas = {
    'data1': {'name': 'Tanglong'},
    'data2': {'interest': 'Computer programming'},
    'data3': {'address': 'Hangzhou China'}
}

class DataOperation(Resource):
    # get data
    def get(self, data_id):
        return {data_id: datas[data_id]}

    # put data
    def put(self, data_id):
        datas[data_id] = request.form['data']
        return {data_id: datas[data_id]}

api.add_resource(DataOperation, '/<string:data_id>')
if __name__ == '__main__':
    app.run(debug=True)
