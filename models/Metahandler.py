from datetime import datetime
    
    
class AModel:
    @staticmethod
    def check_name(name):
        _name=str(name)
        if len(_name)>100:
            return {'message': 'Name of the song cannot be larger than 100'}
        else:
            return _name


    @staticmethod
    def check_duration(duration):
        _duration = int(duration)
        if _duration > 0:
            return _duration
        else:
            return {'message': 'Duration must be positive value'}, 404

    @staticmethod 
    def check_uploaded_time(uploaded_date):
        _uploaded_date=datetime.strptime(uploaded_date, "%Y-%m-%d %H:%M:%S.%f")
        if _uploaded_date.date()< datetime.now().date():
            return {'message': 'Date cannot be in the past'}, 404
        else:
            return _uploaded_date

   
