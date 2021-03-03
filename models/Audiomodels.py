import datetime
from flask import Flask,request
from .db import db, initialize_db
from models.Metahandler import AModel

#using MongoEngine to create our collection 
class Song(db.Document):
    _id = db.IntField(required=True)
    name = db.StringField(max_length=100, required=True)
    duration=db.IntField(required=True)
    uploaded_time=db.DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return '<song %r>' %(self.name)
    
    @staticmethod
    def save_to_db(data):
        if data is not None:
            name=AModel.check_name(data['Name'])
            duration=AModel.check_duration(data['Duration'])
            date=AModel.check_uploaded_time(data['Uploaded_time'])
            all_=Song(_id=data['Id'],name=name, duration=duration, uploaded_time =date)
            all_.save()
            all_details={'Id': data['Id'], 'Name': name, 'Duration': duration,'Uploaded_time': date.__str__()}
            return all_details
        else:
            {"message":"You need to pass the necessary informations"}


class Podcast(db.Document):
    _id = db.IntField(required=True)
    name = db.StringField(max_length=100, required=True)
    duration=db.IntField(required=True)
    uploaded_time=db.DateTimeField(default=datetime.datetime.utcnow)
    host = db.StringField(max_length=100, required=True)
    participants= db.ListField(db.StringField(max_length=100, unique=True), max_length=10)

    def __repr__(self):
        return '< podcast%r>' %(self.name)

    @staticmethod
    def save_to_db(data):
        if data is not None:
            name=AModel.check_name(data['Name'])
            duration=AModel.check_duration(data['Duration'])
            date=AModel.check_uploaded_time(data['Uploaded_time'])
            all_=Podcast(_id=data['Id'],name=name, duration=duration, uploaded_time =date,host=data['host'],participants=data['participants'])
            all_.save()
            all_details={'Id': data['Id'], 'Name': name, 'Duration': duration,'Uploaded_time': date.__str__(),'host':data['host'],'Participants':data['participants']}
            return all_details
        else:
            {"message":"You need to pass the necessary informations"}
    

class Audiobook(db.Document):
    _id = db.IntField(required=True)
    title = db.StringField(max_length=100, required=True)
    author = db.StringField(max_length=100, required=True)
    narrator = db.StringField(max_length=100, required=True)
    duration=db.IntField(required=True)
    uploaded_time=db.DateTimeField(default=datetime.datetime.utcnow)

    def __repr__(self):
        return '< audiobook%r>' %(self.name)
    
    @staticmethod
    def save_to_db(data):
        if data is not None:
            duration=AModel.check_duration(data['Duration'])
            date=AModel.check_uploaded_time(data['Uploaded_time'])
            all_=Audiobook(_id=data['Id'],title=data['title'], author=data['author'],narrator=data['narrator'], duration=data['Duration'],uploaded_time =date)
            all_.save()
            all_details={'Id': data['Id'], 'title': data['title'],'author': data['author'],'narrator':data['narrator'] ,'Duration': duration,'Uploaded_time': date.__str__()}
            return all_details
        else:
            {"message":"You need to pass the necessary informations"}
  
