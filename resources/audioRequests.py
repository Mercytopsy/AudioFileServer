from flask import Flask,request,jsonify



class audioFileHandler:

    @staticmethod
    def create_db(db,data,values,name):
        #we get all collection from our database here
        collection_names=db.get_db().list_collection_names()
        #it checks if the database is empty, if its empty, then we create each audioFiles collections based on our request(i.e. /Song, /Podcast or /Audio) by using specification from Mongoengine schemas defined for each Audiofiles.   
        if collection_names==[]: 
            if name in values.keys():
                audio_file=values[name]
                result=audio_file.save_to_db(data)
                return jsonify({"audoFileType":name,"audioFileMetaData":result})
        else:
            if name in values.keys():
                audio_file_=values[name]
                others=audio_file_.save_to_db(data)
                return jsonify({"audoFileType":name,"audioFileMetaData":others})
            else:
                None
    
    
    #It reads each FIletypes from db based on whichever one we use in our request endpoint
    @staticmethod
    def read_db(values,name,_id): 
        audio_file=values[name]
        result=audio_file.objects(_id=_id).first()
        if result:
            return jsonify({"message":result})
        else:
            {'message':"This AudioFile doesn't exist" },400

    
    @staticmethod
    def delete_from_db(values,name, _id):
        audio_to_delete=values[name]
        query_db=audio_to_delete.objects(_id=_id)
        query_db.delete()
        return {"message": "deleted"}, 200
    
            

    @staticmethod
    def read_all(values, name):
        audio_file=values[name]
        result=audio_file.objects()
        if result is not None:
            return jsonify({"audoFileType":name,"audioFileMetaData":result})
        else:
            {'message':"No AudioFIles in this collection" },400
    
    
    @staticmethod
    def update_audio(values,data,name, _id):
        audio_file = values[name]
        result=audio_file.objects(_id=_id)
        updated_data=result.update(**data)
        return jsonify({'audioFileType':name, "audioFIleMetaData": updated_data})

