# AudioFileServer

## Libraries 

Flask-restful

Flask-MongoEngine


#### Audio file type can be one of the following:

    • Song
    • Podcast
    • Audiobook

The create, read, upload, and delete endpoints are generic and usable for all audio file types,

### POST REQUEST: /Song, /Podcast, /Audiobook

### Response:
{
    "audioFileMetaData": {
        "Duration": 30,
        "Id": 3,
        "Name": "Duduke",
        "Uploaded_time": "2021-03-03 03:00:51.114294"
    },
    "audoFileType": "Song"
}
{
    "audioFileMetaData": {
        "Duration": 1300,
        "Id": 1,
        "Name": "Afar",
        "Participants": [
            "FireBoy, Olamide"
        ],
        "Uploaded_time": "2021-03-03 03:00:51.114294",
        "host": "Ebuka"
    },
    "audoFileType": "Podcast"
}
{
    "audioFileMetaData": {
        "Duration": 1200,
        "Id": 1,
        "Uploaded_time": "2021-03-03 03:00:51.114294",
        "author": "Odafe Atogun",
        "narrator": "Prentice Onayemi,
        "title": "Taduno's Song"
    },
    "audoFileType": "Audiobook"
}
