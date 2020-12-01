from konlpy.tag import Hannanum
from newsParser import han
import build_hannanum

if __name__ == '__main__':
    build_hannanum.build()
    hannanum = Hannanum()
    print(han('더불어민주당이 일한다', [], None, hannanum))
