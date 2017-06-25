# make sure you have the following packages
# pip install flask flask-jsonpify flask-sqlalchemy flask-restful

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from json import dumps
from flask.ext.jsonpify import jsonify
decisionmaker = __import__('decisionmaker')

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

class Room_Emotion(Resource):
	def get(self, r_type, current_genre):
		print('requesting recognition: ' + r_type)
		decision = decisionmaker.getDecisionForSongChange(r_type)
		return jsonify(decision)
        
api.add_resource(Room_Emotion, '/api/genre/next/<r_type>/<current_genre>')

if __name__ == '__main__':
     app.run(port='5002')
