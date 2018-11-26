import os

DEBUG = True
MONGO_URI = 'mongodb://localhost:27017/automateLock_db'
SECRET_KEY = '123456'
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads/')
STATIC_F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/')
CACHE_TYPE = "null"
