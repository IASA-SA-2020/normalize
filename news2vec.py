from konlpy.tag import Hannanum
import build_hannanum
import os
from gensim.models.word2vec import Word2Vec
from newsParser import parseNews
from db import loadNews, connectDB

host = 'mongodb://user:iasa2020!@localhost'

chunk = 100

if __name__ == '__main__':
    build_hannanum.build()
    hannanum = Hannanum()

    print('Load Parser Done!')

    filedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'w2v')
    os.chdir(filedir)
    w2v = Word2Vec.load('model.model')
    print('Load Word2Vector Done!')
    _, _, _, _, vecDB, *_ = connectDB(host)

    try:
        begin = vecDB['metadata'].find_one({'type': 'politics'})['idx']
    except:
        begin = 0

    while True:
        wv = []
        li = loadNews(chunk, begin)

        for i in li:
            wv += parseNews(i, (hannanum, w2v))
            print('parse')

        begin += len(li)
        if wv:
            vecDB['data'].insert_many(wv)
            print('Pushed %d wv(s) to DB.' % len(wv))
        vecDB['metadata'].insert_one({'type': 'politics', 'idx': begin})
