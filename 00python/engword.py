# pip install googletrans==4.0.0-rc1
# from googletrans import Translator
# pip install deep-translator

from deep_translator import GoogleTranslator

words = {}


def regist():
    s = input("등록할 단어:")
    
    if s in words:
        print('등록된 단어임')
    else:
        words[s] = GoogleTranslator(source='auto', target='en').translate(s)
        print(f"{s} → (등록됨)")


def quiz():
    for key,value in words.items():
        ans = input(key+'영어이름은?')
        if ans == value:
            print("ok")
        else:
            print("on, no")


while True:
    sel = int(input("1.등록, 2.퀴즈, 3.종료 :"))
    if sel == 3:
        print("종료")
        break
    elif sel == 1:
        regist()
    elif sel==2:
        quiz()
    else:
        print("잘못입력")
