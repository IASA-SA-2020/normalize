import shutil
import os


def read_file(name, post):
    li = []
    f = open("userdict/" + name, 'rt', encoding='utf-8')
    while True:
        line = f.readline()
        if not line:
            break
        if not line.strip():
            continue
        if not post:
            li.append(line.strip())
        else:
            li.append(line.strip().replace(' ', '') + '\t' + post)
    f.close()
    return li


def build():
    li = read_file('person/first', 'nqpa')
    li += read_file('person/criminal', 'nqpc')
    li += read_file('person/famous', 'nqpc')
    li += read_file('person/politician', 'nqpc')
    li += read_file('org/company', 'nqq')
    li += read_file('org/gov', 'nqq')
    li += read_file('org/party', 'nqq')
    li += read_file('position', 'nqq')
    li += read_file('new/verb', '')
    li += read_file('new/noun_work', 'ncpa')
    li = list(set(li))

    with open('./konlpy/java/data/kE/dic_user.txt', 'wt', encoding='utf-8') as f:
        f.write('\n'.join(li))

    print('Build user dict Done!')


if __name__ == '__main__':
    build()
