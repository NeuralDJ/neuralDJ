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
FirstCall = True

class Room_Emotion(Resource):
	def get(self, current_genre):
		#run something
        #print(current_genre)
        #Call getDecisionForSongChange to with 'features' to get age,gender of room
        #Call getDecisionForSongChange to with anything else to get decision to change song
		global FirstCall
		if FirstCall:
			decision = decisionmaker.getDecisionForSongChange('features')
		else:
			decision = decisionmaker.getDecisionForSongChange()
		FirstCall = False
		print(decision)
		return jsonify(decision)
        

api.add_resource(Room_Emotion, '/api/genre/next/<current_genre>') #Route_3

if __name__ == '__main__':
     app.run(port='5002')
