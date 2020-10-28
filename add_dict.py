def proc():
    str = input()
    fp = open('./dict/person.dic', mode='rt', encoding='utf-8')
    while True:
        line = fp.readline()
        if not line:
            break
        if str in line:
            return
    fp.close()

    fp = open('./dict/person.dic', mode='at', encoding='utf-8')
    fp.write('\n%s/NNP' % str)
    fp.close()
    print('Added!')


while True:
    proc()
