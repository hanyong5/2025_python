from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)



def main():
    with open("data/news.txt",'r',encoding='utf-8') as f:
        text = f.read()
    prompt = f'''
        You are an AI specialized in summarizing news articles.  
        Please summarize the following article in **3 concise sentences**, focusing only on the key points.

        ✅ Summary Guidelines:  
        - Include key information such as main figures, events, time, location, cause, and outcome  
        - Avoid repetition; keep it concise  
        - Use an objective and neutral tone

        ** text : {text} **

        3-Sentence Summary:
        1.  
        2.  
        3.

        **finally, provide your full answer in korean**

        
    '''
    response =  client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system","content":"You are a great assistant in summarizing text in Korean."},
            {"role":"user","content":prompt}
        ]
    )
    summary = response.choices[0].message.content
    print(summary)

if __name__ == "__main__":
    main()