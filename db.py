import pymongo

def connectDB(host):
    while True:
        try:
            conn = pymongo.MongoClient(host, 27017)
            newsDB = conn["newsDB"]
            categoryDB = conn["newsCategory"]
            newsRawDB = conn["newsRawDB"]
            wordDB = conn["wordDB"]
            return newsDB, categoryDB, newsRawDB, wordDB
        except:
            pass
