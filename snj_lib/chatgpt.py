import openai
from dotenv import load_dotenv
import os

def print_chatgpt():
    load_dotenv()
    openai_key = os.environ.get('openai')
    openai.api_key = openai_key


    #모델 설정하기
    model = "gpt-3.5-turbo"
    # 질문 작성하기
    query = input("질문을 알려주세요 : ")
    # 메시지 설정하기
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
    ]

    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    print(answer)
