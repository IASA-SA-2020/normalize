import shutil
import os



if __name__ == '__main__':
    try:
        shutil.rmtree('./kkma/dic')
        os.remove('./kkma-2.0.zip')
    except:
        pass
    shutil.copytree('./dict', './kkma/dic')

    try:
        os.remove('./konlpy/java/kkma-2.0.jar')
    except:
        pass

    os.system('cd kkma && jar -cvf kkma-original.jar/ .')

    shutil.move('./kkma/kkma-original.jar', './konlpy/java/kkma-2.0.jar')
    try:
        os.remove('./kkma/kkma-original.jar')
    except:
        pass
