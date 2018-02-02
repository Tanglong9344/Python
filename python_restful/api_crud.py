# some methods(crud) on resources
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

datas = {
    'data1': {'name': 'Tanglong'},
    'data2': {'interest': 'Computer programming'},
    'data3': {'address': 'Hangzhou China'}
}


def abort_if_data_doesnt_exist(data_id):
    if data_id not in datas:
        abort(404, message="datas[{}] doesn't exist".format(data_id))

parser = reqparse.RequestParser()
parser.add_argument('data')


# data
# shows a single data item and lets you delete a data item
class data(Resource):
    def get(self, data_id):
        abort_if_data_doesnt_exist(data_id)
        return datas[data_id]

    def delete(self, data_id):
        abort_if_data_doesnt_exist(data_id)
        del datas[data_id]
        return '', 204

    def put(self, data_id):
        args = parser.parse_args()
        data = {'data': args['data']}
        datas[data_id] = data
        return data, 201


# dataList
# shows a list of all datas, and lets you POsT to add new tasks


class dataList(Resource):
    def get(self):
        return datas

    def post(self):
        args = parser.parse_args()
        data_id = int(max(datas.keys()).lstrip('data')) + 1
        data_id = 'data%i' % data_id
        datas[data_id] = {'task': args['task']}
        return datas[data_id], 201


# Actually setup the Api resource routing here
api.add_resource(dataList, '/datas')
api.add_resource(data, '/datas/<data_id>')

if __name__ == '__main__':
    app.run(debug=True)
