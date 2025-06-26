from deep_translator import GoogleTranslator

def google_trans(messages):
    result = GoogleTranslator(source='auto',target='ko').translate(messages)
    return result


text = f'''
Prompt engineering is the process of writing effective instructions for a model, such that it consistently generates content that meets your requirements.
Because the content generated from a model is non-deterministic, it is a combination of art and science to build a prompt that will generate content in the format you want. However, there are a number of techniques and best practices you can apply to consistently get good results from a model.
Some prompt engineering techniques will work with every model, like using message roles. But different model types (like reasoning versus GPT models) might need to be prompted differently to produce the best results. Even different snapshots of models within the same family could produce different results. So as you are building more complex applications, we strongly recommend that you:
'''

result = google_trans(text)
print(result)