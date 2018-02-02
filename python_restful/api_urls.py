# add one more urls
# reference: http://flask-restful.readthedocs.io/en/0.3.5/quickstart.html
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)  # set current file as a API
datas = {'data_id1': 'data111', 'data_id2': 'data222', 'data_id3': 'data333'}


class EndPoint(Resource):
    # get data
    def get(self, data_id):
        return {data_id: datas[data_id]}


api.add_resource(EndPoint, '/data/<string:data_id>', endpoint='data_ep')
if __name__ == '__main__':
    app.run(debug=True)
