from deep_translator import GoogleTranslator

# 저장소
words = {}

# 함수
def regist():
    q = input("등록할 단어 : ")

    if q in words:
        print(f'{q} 는 등록단어')
        print("="*20)
    else:
        words[q] = GoogleTranslator(source='auto',target='en').translate(q)
        print(f'{q} 단어가 등록됨')

def quiz():
    for key,value in words.items():
        ans = input(key + "영어단어작성")
        if ans == value:
            print("정답입니다")
        else:
            print("oh!!!! no")




# 실행
while True:
    select = int(input("1.등록,2.퀴즈,3.종료 : "))
    if select == 3:
        print("종료")
        break

    elif select == 1:
        # print("단어등록")
        regist()
    
    elif select == 2:
        # print("퀴즈시작")
        quiz()

    else:
        print("잘못입력")