from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
elmain = __import__('main')

app = Flask(__name__)
api = Api(app)

class Room_Emotion(Resource):
    def get(self, current_genre):
        #run something
        #print(current_genre)
        next_genre = elmain.run_program()
        return jsonify(next_genre)

api.add_resource(Room_Emotion, '/api/genre/next/<current_genre>') # Route_3

if __name__ == '__main__':
     app.run(port='5002')