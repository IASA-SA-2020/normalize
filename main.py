import soynlp.lemmatizer as lem
from konlpy.tag import Hannanum, Kkma
from get_news import getRandomNews
import re


def onlyHangul(str):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('', str)
    return result


def log(obj):
    return
    print(obj)


hannanum = Hannanum()
kkma = Kkma()

str = getRandomNews()


def han(sentence):
    orgP = hannanum.pos(sentence)
    print(orgP)

    nounList = []
    for i in hannanum.nouns(sentence):
        hangul = onlyHangul(i)
        if hangul:
            nounList.append(hangul)

    log(nounList)

    an = hannanum.analyze(sentence)
    anSel = []

    print(an)

    for i in an:
        log(i)
        sel = i[0]
        maxScore = 0
        currentScore = 0
        for p in i:
            currentScore = 1
            for j in range(len(p)):
                if len(orgP) <= len(anSel) + j or orgP[len(anSel) + j][1].lower() != p[j][1][0] \
                        or orgP[len(anSel) + j][0] != p[j][0]:
                    currentScore = -1
                    break
                if p[j][1][0] == 's':
                    continue
                if p[j][1][0:2] == 'nq':
                    currentScore += 2
                if not (p[j][1][0] == 'n'):
                    currentScore += 1
                if p[j][0] in nounList:
                    currentScore += 5
            if maxScore < currentScore:
                maxScore = currentScore
                sel = p
        for j in sel:
            anSel.append(j)

    for i in anSel[:]:
        if i[1][0:2] == 'pa':
            anSel.remove(i)
        if i[1][0:2] == 's':
            anSel.remove(i)
    return anSel


def kk(sentence):
    print(kkma.pos(sentence))


for sentence in str.split('.'):
    sentence = sentence.strip()

    if not sentence:
        continue

    sentence = '~'.join(sentence.split('"')[::2])

    anSel = kk(sentence)

    print(anSel)
