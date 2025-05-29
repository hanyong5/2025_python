from tkinter import Tk, Label, Entry, Button, Text, END
from deep_translator import GoogleTranslator


def translate_text():
    input_text = entry.get()
    if input_text.strip():
        try:
            result = GoogleTranslator(source='auto', target='en').translate(input_text)
            output.delete(1.0, END)
            output.insert(END, result)
        except Exception as e:
            output.delete(1.0, END)
            output.insert(END, f"오류: {e}")

root = Tk()
root.title("간단 번역기")
root.geometry("400x250")

Label(root, text="번역할 문장:").pack(pady=(10, 0))
entry = Entry(root, width=50)
entry.pack(pady=5)

Button(root, text="번역", command=translate_text).pack(pady=5)

Label(root, text="번역 결과:").pack(pady=(10, 0))
output = Text(root, height=5, width=50)
output.pack(pady=5)

root.mainloop()
