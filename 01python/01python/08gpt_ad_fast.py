from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()
#uvicorn 08gpt_ad_fast:app --reload 

class AdRequest(BaseModel):
    name:str
    strenghth:str
    keyword:str
    com_name:str
    tone_manner:str
    value:str
    api_key:str

@app.get("/")
def test_get():
    return {"message":"fast API test****"}


@app.get("/han")
def test_get1():
    return {"message":"fast API test****"}


def ask_gpt(prompt,apikey):
    try:
        client = openai.OpenAI(api_key = apikey)
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role":"user","content":prompt}
            ])
        gptRes = response.choices[0].message.content
        return gptRes

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

  


@app.post("/ad")
def generate_ad(req:AdRequest):
    prompt = f'''
        아래의 내용을 참고해서 1~2줄짜리 광고문구 5개 작성해줘
        - 제품명:{req.name}
        - 제품특징:{req.strenghth}
        - 필수포함키워드:{req.keyword}
        - 브랜드명:{req.com_name}
        - 톤엔매너:{req.tone_manner}
        - 브랜드핵심가치:{req.value}
        '''

    ads = ask_gpt(prompt,req.api_key)
    return {"result":ads}