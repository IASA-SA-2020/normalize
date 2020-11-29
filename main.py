from konlpy.tag import Hannanum, Kkma
from get_news import getRandomNews
import re
from detect import is_human, is_org, is_pos
import build_hannanum
import os
from gensim.models.word2vec import Word2Vec



def onlyHangul(str):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('', str)
    return result


def log(obj):
    return
    print(obj)



def han(sentence, humanList, lastSubject):
    orgP = hannanum.pos(sentence)
    # print(orgP)

    nounList = []
    for i in hannanum.nouns(sentence):
        hangul = onlyHangul(i)
        if hangul:
            nounList.append(hangul)

    log(nounList)

    an = hannanum.analyze(sentence)
    an_sel = []

    # print(an)

    for i in an:
        log(i)
        sel = i[0]
        maxScore = 0
        currentScore = 0
        for p in i:
            currentScore = 1
            for j in range(len(p)):
                if len(orgP) <= len(an_sel) + j or orgP[len(an_sel) + j][1].lower() != p[j][1][0] \
                        or orgP[len(an_sel) + j][0] != p[j][0]:
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
            an_sel.append(j)

    print(an_sel)

    subject = None
    subject_hubo = []

    fl = False
    for i in range(len(an_sel)):
        if an_sel[i][1][0] == 'j' and (
                an_sel[i][0] == '은' or an_sel[i][0] == '는' or an_sel[i][0] == '이' or an_sel[i][0] == '가' or (
                '께서' in an_sel[i][0]) or ('이서' in an_sel[i][0])) and (
                i == len(an_sel) - 1 or an_sel[i + 1][1][0] != 'e'):
            fl = True
            break
        if an_sel[i][1][0] == 'n':
            subject_hubo.append(an_sel[i][0])
            if is_human(an_sel[i][0]):
                humanList.append(an_sel[i][0])
    if not fl:
        subject_hubo = []

    for i in subject_hubo:
        if is_org(i):
            subject = i

    for i in subject_hubo:
        if is_pos(i):
            try:
                for k in range(sentence.index(i) - 1, sentence.index(i) - 3, -1):
                    first = sentence[k]
                    for j in humanList:
                        if j[0] == first:
                            subject = j
                    try:
                        if not subject:
                            subject = i
                    except:
                        subject = i
            except:
                pass

    for i in subject_hubo:
        if is_human(i):
            subject = i

    if not subject:
        if '이어' in sentence or '또한' in sentence or '그리고' in sentence:
            subject = lastSubject

    verb_list = []
    for i in an_sel:
        if i[1][0] == 'p':
            verb_list.append(i[0] + '다')
        if i[1][:3] == 'ncp':
            verb_list.append(i[0] + '하다')

    main_verb = None

    if not main_verb:
        main_verb = verb_list[-1]

    return subject, main_verb, hannanum.nouns(sentence), verb_list


if __name__ == "__main__":
    build_hannanum.build()
    hannanum = Hannanum()
    kkma = Kkma()
    print('Load Parser Done!')

    str = getRandomNews()
    print('Load News Done!')

    filedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'word2vec')
    os.chdir(filedir)
    model = Word2Vec.load('mini_namu.model')
    print('Load word2vec Done!')

    humanList = []
    anSel = [None]

    for sentence in str.split('.'):
        sentence = sentence.strip()

        if not sentence:
            continue

        anSel = han(sentence, humanList, anSel[0])

        print(anSel)
