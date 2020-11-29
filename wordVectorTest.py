import os
import time
from gensim.models.word2vec import Word2Vec

if __name__ == "__main__":
    filedir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(filedir)
    filename4 = 'mini_namu.model'


    print('Model test')
    t1 = time.time()
    model = Word2Vec.load(filename4)
    t2 = time.time()
    print(model.wv.similarity('놀다', '일하다'))

    print('time=', t2 - t1)
