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
            vecDB = conn["vecDB"]
            return newsDB, categoryDB, newsRawDB, wordDB, vecDB
        except:
            pass


def loadNews(chunk, begin=0):
    newsDB, categoryDB, *_ = connectDB(host)
    li = list(categoryDB['politics'].find().skip(begin).limit(chunk))
    newsList = []

    for i in li:
        oid = '%03d' % i['oid']
        aid = i['aid']
        newsList.append(newsDB[oid].find_one({'newsId': aid})['summary'])

    return newsList
