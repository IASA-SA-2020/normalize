import random

newsDB = [
    ''''친조국' 인사인 김남국 더불어민주당 의원은 21일 민주당에서 탈당한 금태섭 전 의원을 향해 "자신의 이익과 자리만 쫓아 다니는 철새 정치인"이라고 했다.
    김 의원은 금 전 의원이 민주당을 탈당한 이유로 세 가지를 주장했다.
    국민의힘에 입당해 내년 서울시장 재보궐 선거나 지역구 재보궐을 준비하려는 것, 민주당에서 한 번 더 국회의원 하기는 쉽지 않을 것 같으니 하루라도 빨리 다른 당으로 가서 자리를 잡자는 조급함, 탈당한 뒤 중간지대에 있으면서 대선판에서 기회를 찾자는 생각 등이다.'''

    ,

    '''홍준표 무소속 의원이 28일 국민의힘 지도부를 겨냥해 또다시 비판의 목소리를 냈다.
    전날 의원총회에서도 지도부를 향해 이같은 불만이 나왔다.
    한편 홍 의원은 전날에도 페이스북에서 국민의힘을 향해 "병력도 더불어민주당의 절반밖에 안 되고 결기도 보이지 않는 야당이 그 안에서 저 세력은 극우라서 손절하고, 저 사람은 강성이라서, 저 사람은 나와 악연이 있어서, 저 사람은 내가 당권을 잡는데 방해가 되니 배제한다"고 비판한 바 있다.'''

    ,

    '''장하성 중국 주재 한국대사는 21일 방탄소년단의 수상 소감 논란으로 인한 '중국 내 BTS 굿즈 배송 중단' 상황에 대해 중국 고위급에 문제를 제기했다고 밝혔다. 
    이어 "윈다라는 업체가 공지를 올린 이후 두 업체가 중단했다는 보도가 있어 직접 확인했는데 일단 중단 조치는 없었다"면서 "하지만 분명 배달 중지 문제가 생겼기 때문에 매우 적극적으로 대응하고 있고, 국감이 끝나면 중국 고위층에 직접 문제를 제기하겠다"고 답했다. 
    장 대사는 또 BTS 굿즈 배송 중단 업체가 확대되고 있다는 언론 보도와 관련해서는 "처음에 윈다라는 업체 한 곳이었는데 중퉁 등 다른 업체가 추가됐다는 보도가 나와서 업체들과 직접 소통하고 있다"면서 "워낙 민감하고 양국 국민 감정선을 건드릴 수 있기 때문에 엄중하게 대응하고 있다"고 답했다.'''
]


def getRandomNews():
    return newsDB[1]
    return newsDB[random.randint(0, len(newsDB) - 1)]
