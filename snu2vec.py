from konlpy.tag import Hannanum
import build_hannanum
import os
from gensim.models.word2vec import Word2Vec
from newsParser import parseSNU
from db import loadSNU, connectDB

host = 'localhost'

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
        begin = vecDB['metadata'].find_one({'type': 'snu'})['idx']
    except:
        begin = 0

    while True:
        wv = []
        li = loadSNU(chunk, begin)
        for i in li:
            wv += parseSNU(i, (hannanum, w2v))
        begin += len(li)
        if wv:
            vecDB['snu'].insert_many(wv)
            print('Pushed %d wv(s) to DB.' % len(wv))
        vecDB['metadata'].delete_one({'type': 'snu'})
        vecDB['metadata'].insert_one({'type': 'snu', 'idx': begin})
