import os
import pymongo


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app', 'static')
    ALLOWED_EXTENSIONS = ["JSON"]
    MAX_CONTENT_LENGTH = 16 * 1024 * 100024
<<<<<<< HEAD:ingestion/config.py
    # URI = 'mongodb://127.0.0.1:5000'
    # MONGO_CLIENT = pymongo.MongoClient('mongodb://127.0.0.1:5000',27017)
    CLIENT = pymongo.MongoClient(
        'mongodb://DB:27017/vizrec' or 'localhost', 27017)
    DB = CLIENT['test']
    VIZREC = DB.vizrec
    HOST = '0.0.0.0'
=======
    URI = 'mongodb://127.0.0.1:27017'
    CLIENT = pymongo.MongoClient(URI)
    DB = CLIENT['test']
    VIZREC = DB.VIZREC
>>>>>>> master:inference/config.py
