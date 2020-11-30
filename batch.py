from konlpy.tag import Hannanum
import build_hannanum
import os
from gensim.models.word2vec import Word2Vec
from newsParser import parseNews
from get_news import getRandomNews
from db import loadNews

if __name__ == '__main__':
    build_hannanum.build()
    hannanum = Hannanum()

    print('Load Parser Done!')

    filedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'w2v')
    os.chdir(filedir)
    w2v = Word2Vec.load('model.model')
    print('Load Word2Vector Done!')

    str = getRandomNews()
    print('Load News Done!')
    print(len(parseNews(str, (hannanum, w2v))))
