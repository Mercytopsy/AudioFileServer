import os
from flask import Flask,request
from flask_restful import Api,Resource,reqparse
from flask_mongoengine import MongoEngine
from settings import DB, DATABASE_USERNAME, DATABASE_PASSWORD
from models.Audiomodels import Song,Podcast,Audiobook
from resources.audioRequests import audioFileHandler

app = Flask(__name__)
db = MongoEngine()


app.config['MONGODB_SETTINGS'] = {
'db': os.getenv(DB),
'username':os.getenv(DATABASE_USERNAME),
'password':os.getenv(DATABASE_PASSWORD)
}
db.init_app(app)

api=Api(app)


class Audio(Resource):

    def post(self, name): 
        data= request.get_json()
        values={'Song':Song,'Podcast':Podcast,'Audiobook':Audiobook}
        db=MongoEngine(app)
        result=audioFileHandler.create_db(db,data,values,name)
        return result

    def get(self, name):
        values={'Song':Song,'Podcast':Podcast,'Audiobook':Audiobook}
        all_fileTypes=audioFileHandler.read_all(values, name)
        return all_fileTypes

class AudioId(Resource):

    def get(self, name, _id): 
        values={'Song':Song,'Podcast':Podcast,'Audiobook':Audiobook}
        result=audioFileHandler.read_db(values,name,_id)
        return result
    
    def delete(self, name, _id):
        values={'Song':Song,'Podcast':Podcast,'Audiobook':Audiobook}
        result = audioFileHandler.delete_from_db(values, name, _id)
        return result
    
    def put(self, name,_id):
        data= request.get_json()
        values={'Song':Song,'Podcast':Podcast,'Audiobook':Audiobook}
        result = audioFileHandler.update_audio(values,data,name,_id)
        return result

api.add_resource(Audio, '/<string:name>')
api.add_resource(AudioId, '/<string:name>/<int:_id>') 
if __name__ == "__main__":
    app.run(debug=True)