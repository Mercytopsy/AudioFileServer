try:
    from applications import app

    import unittest
    import json
#from models.songs import SongModel
except Exception as e:
    print("Some Modules are Missing {}".format(e))

class AudioTest(unittest.TestCase):

      #Testing for the song post request

 
    def test_create_song(self):
        # Given
        payload = json.dumps({"Id":1, "Name": "Onyeka",
        "Duration": 30, 
        "Uploaded_time": "2021-03-03 03:00:51.114294"})

        response = app.test_client().post('/Song', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(200, response.status_code)


    
    #check responses for each AudioFIleType endpoint, if it gives 200 status code
    def test_song(self):
        tester = app.test_client(self)
        response = tester.get("/Song")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_podcast(self):
        tester = app.test_client(self)
        response = tester.get("/Podcast")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_audiobook(self):
        tester = app.test_client(self)
        response = tester.get("/Audiobook")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #check one of the filetypes by changing the status code to 400 
    def test_song_dif(self):
        tester = app.test_client(self)
        response = tester.get("/Song")
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    
    #check responses by testing for each audiofile id endpoint 
    def test_song_id(self):
        tester = app.test_client(self)
        response = tester.get("/Song/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_podcast_id(self):
        tester = app.test_client(self)
        response = tester.get("/Podcast/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_audio_id(self):
        tester = app.test_client(self)
        response = tester.get("/Audiobook/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #Test one of the AudioFile if contents return json file 
    def test_song_content(self):
        tester = app.test_client(self)
        response = tester.get('/Song')
        self.assertEqual(response.content_type, "application/json")

  


if __name__ == "__main__":
    unittest.main( )