# Sets up basic server
# Copied directly from the Flask webpage
# http://flask-restful-cn.readthedocs.io/en/0.3.4/quickstart.html

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
