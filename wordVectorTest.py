import os
import time
from gensim.models.word2vec import Word2Vec

if __name__ == "__main__":
    filedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'w2v')
    os.chdir(filedir)
    filename4 = 'model.model'

    model = Word2Vec.load(filename4)
    print('Model Loaded!')
    while True:
        try:
            (a, b) = input().split(' ')
            print(model.wv.similarity(a, b))
        except:
            pass
