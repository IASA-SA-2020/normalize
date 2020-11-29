# 문장 단위로 나누기
# 문장의 주어, 동사, 형용사 찾기
# 기본 dataset 구성 - 주어, 목적어는 nounlist에 추가, 동사는 verblist에 추가
# 정리된 dataset 구성 - {'명사' : (목적어의 존재여부, (동사, 긍정(1)/부정(0)), 목적어) } 로 데이터 묶기

from konlpy.tag import Kkma, Hannanum


if __name__ == '__main__':
    kkma = Kkma()
    hannanum = Hannanum()
    # 가공할 문자열 data
    data = "나는 꽃을 좋아합니다. 나는 코스모스가 제일 좋습니다. 나는 달리고 있습니다."
    TotalNounList = set()  # data에 등장하는 모든 noun 저장
    ProcessDataSet = dict()  # 가공한 dataset

    # 문장 단위로 분리하기
    SentenceList = data.split('.')

    for sentence in SentenceList:
        sentence = sentence.strip()

        # case1) 문장이 아닌 경우
        if not sentence:
            continue

        # case2) 문장인 경우
        # 주어 찾기(noun) - 체언(N), 관계언(J) -> 주격조사(jcs)
        # 목적어 찾기(object) - 체언(N), 관계언(J) -> 목적격조사(jco)
        # 동사 찾기(verb) - 용언(P) -> 동사(pv-)
        WordList = sentence.split(' ')  # 단어 단위로 분리하기

        tempNList = []  # 문장에 등장하는 명사
        tempPList = []  # 문장에 등장하는 동사
        tempS = False  # 문장에 등장하는 주어
        # 주어가 여러 개일 경우 고려
        tempO = False  # 문장에 등장하는 목적어
        # 목적어가 여러 개일 경우 고려

        for word in WordList:
            IsP = False
            IsN = False
            WordAnalysis = kkma.pos(word)  # ex) [('서','P'), ('어', 'E'),...]
            for i in WordAnalysis:
                if i[1][0] == 'P':  # 용언이라고 판명되는 것을 포함하는 경우
                    IsP = True
                    break
                if i[1][0] == 'N':  # 체언이라고 판명되는 것을 포함하는 경우
                    IsN = True
                    tempNList.append(i[0])  # 단어를 이루는 요소 중 체언만을 저장(조사와 같은 것을 삭제)
                    break
            TotalNounList.update(tempNList)

            # 용언 중에서 동사라고 판명되는 경우 - 문장 내 등장하는 동사를 저장하는 저장하는 list에 저장
            if IsP:
                IsPV = False
                verbAnalysis = hannanum.analyze(word)[0]
                # analyze한 값 : [[[('좋', 'paa'), ('습니다', 'ef')], [('좋', 'px'), ('습니다', 'ef')]]]
                # analyze 한 것이 하나의 단어만으므로
                # testcode : print(word, verbAnalysis)
                # 현재는 동사라고 판명되는 분석결과가 하나라도 있으면 동사라고 취급하고 list에 추가
                # 이후에 가중치 부과하여 동사일 확률이 높을 추가하는 방향으로 개선 필요
                for i in verbAnalysis:  # ex) i = [('좋', 'paa'), ('습니다', 'ef')]
                    for j in i:  # ex) j = ('좋', 'paa')
                        if j[1][:2] == 'pv':
                            IsPV = True
                        break
                    if IsPV:
                        break
                if IsPV:
                    tempPList.append(word)

            if IsN:
                tempNoun = word  # 조사를 포함하는 체언
                print(hannanum.analyze(word))
                nounAnalysis = hannanum.analyze(word)[0]
                # testcode : print(nounAnalysis)
                for i in nounAnalysis:  # nounAnalysis : [[('코스모스', 'ncn'), ('가', 'jcc')], [('코스모스', 'ncn'), ('가', 'jcs')]]
                    temp = i[0][0]
                    # testcode : print('temp :', temp)
                    for j in i:  # i : [('코스모스', 'ncn'), ('가', 'jcc')]
                        # testcode : print('j :', j)
                        if j[1] == 'jcs' or j[1] == 'jxc':  # 주격조사를 포함하는 경우
                            tempS = True
                        # testcode : print('tempS', 'tempO', tempS, tempO)

                    if tempS:
                        tempS = temp
                    if not (tempS and tempO):
                        break

        # testcode : print('tempS', tempS)
        if tempS:  # 주어가 있는 경우
            # 주어가 없는 경우 어떻게 처리할 것인지 고려
            if tempO:
                temp = (1, tempPList, tempO)
            else:
                temp = (0, tempPList, None)
            # testcode : print('temp', temp); print('tempS', tempS, 'keys', ProcessDataSet.keys())

            if tempS in ProcessDataSet.keys():
                ProcessDataSet[tempS].append(temp)
            else:
                ProcessDataSet[tempS] = [temp]

    print(TotalNounList)
    print(ProcessDataSet)
