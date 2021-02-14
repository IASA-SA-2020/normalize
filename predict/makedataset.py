from db import connectDB
import pandas as pd

host = 'localhost'
ds_size = 10000
test_rate = 0.1

if __name__ == '__main__':
    _, _, _, _, vecDB, *_ = connectDB(host)
    li = list(vecDB['data'].find().limit(ds_size))
    ls = list(vecDB['snu'].find())
    print(1)
    test_size = int(len(li) * test_rate)
    test_size_s = int(len(ls) * test_rate)
    test_ds = []
    train_ds = []
    for i in range(test_size):
        try:
            if len(li[i]['nounlist']) > 50 or len(li[i]['verblist']) > 30:
                continue
            if li[i]['fact']:
                ds_one = [5.0]
            else:
                ds_one = [1.0]
            ds_one += li[i]['subject']
            ds_one += li[i]['mainverb']
            for j in li[i]['nounlist']:
                ds_one += j
            for j in range((50 - len(li[i]['nounlist'])) * 200):
                ds_one.append(0)
            for j in li[i]['verblist']:
                ds_one += j
            for j in range((30 - len(li[i]['verblist'])) * 200):
                ds_one.append(0)
            test_ds.append(ds_one)
        except:
            pass

    test_ds = []
    train_ds = []
    for i in range(test_size_s):
        try:
            if len(ls[i]['nounlist']) > 50 or len(ls[i]['verblist']) > 30:
                continue
            ds_one = [ls[i]['score']]
            if ds_one[0] == 3:
                continue
            ds_one += ls[i]['subject']
            ds_one += ls[i]['mainverb']
            for j in ls[i]['nounlist']:
                ds_one += j
            for j in range((50 - len(ls[i]['nounlist'])) * 200):
                ds_one.append(0)
            for j in ls[i]['verblist']:
                ds_one += j
            for j in range((30 - len(ls[i]['verblist'])) * 200):
                ds_one.append(0)
            test_ds.append(ds_one)
        except:
            pass

    test_pd = pd.DataFrame(test_ds)
    test_pd.to_csv('dataset/simple/test.csv', header=False, index=False)
    print(1)
    test_ds = None
    test_pd = None

    for i in range(test_size, len(li)):
        try:
            if len(li[i]['nounlist']) > 50 or len(li[i]['verblist']) > 30:
                continue
            if li[i]['fact']:
                ds_one = [5.0]
            else:
                ds_one = [1.0]
            ds_one += li[i]['subject']
            ds_one += li[i]['mainverb']
            for j in li[i]['nounlist']:
                ds_one += j
            for j in range((50 - len(li[i]['nounlist'])) * 200):
                ds_one.append(0)
            for j in li[i]['verblist']:
                ds_one += j
            for j in range((30 - len(li[i]['verblist'])) * 200):
                ds_one.append(0)
            train_ds.append(ds_one)
        except:
            pass

    test_ds = []
    train_ds = []
    for i in range(test_size_s, len(ls)):
        try:
            if len(ls[i]['nounlist']) > 50 or len(ls[i]['verblist']) > 30:
                continue
            ds_one = [ls[i]['score']]
            if ds_one[0] == 3:
                continue
            ds_one += ls[i]['subject']
            ds_one += ls[i]['mainverb']
            for j in ls[i]['nounlist']:
                ds_one += j
            for j in range((50 - len(ls[i]['nounlist'])) * 200):
                ds_one.append(0)
            for j in ls[i]['verblist']:
                ds_one += j
            for j in range((30 - len(ls[i]['verblist'])) * 200):
                ds_one.append(0)
            train_ds.append(ds_one)
        except:
            pass

    train_pd = pd.DataFrame(train_ds)
    train_pd.to_csv('dataset/simple/train.csv', header=False, index=False)
