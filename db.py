import pymongo

host = 'mongodb://user:iasa2020!@localhost'


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


def loadNews(chunk):
    newsDB, categoryDB, _, __ = connectDB(host)
    li = list(categoryDB['politics'].find().limit(chunk))
    newsList = []
    for i in li:
        oid = '%03d' % i['oid']
        aid = i['aid']
        newsList.append(newsDB[oid].find_one({'aid': aid})['summary'])

    return newsList
