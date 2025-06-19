from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os
import time
import tempfile

def translate_and_speak():
    print("=== 번역 + 일본어 음성 출력기 (pygame + 임시파일 안전처리) ===")

    # pygame 초기화
    pygame.mixer.init()

    while True:
        text = input("번역할 한국어 문장을 입력하세요 (종료하려면 'exit'): ")
        if text.lower() == 'exit':
            print("프로그램을 종료합니다.")
            break

        try:
            # 1. 번역 수행
            translated = GoogleTranslator(source='ko', target='ja').translate(text)
            print(f"일본어 번역: {translated}")

            # 2. 임시 디렉터리에서 mp3 파일 생성
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts = gTTS(translated, lang='ja')
                tts.save(fp.name)
                voice_path = fp.name

            # 3. pygame으로 음성 재생
            pygame.mixer.music.load(voice_path)
            pygame.mixer.music.play()

            # 4. 재생 완료까지 대기
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)

            # 5. 파일 사용 끝난 후 삭제
            pygame.mixer.music.unload()  # 파일 닫기
            os.remove(voice_path)

        except Exception as e:
            print(f"오류 발생: {e}\n")

if __name__ == "__main__":
    translate_and_speak()
