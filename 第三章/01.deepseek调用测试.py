# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
#创建与ai大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是Deep seek的apikey）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com/v1")
#与ai大模型进行交互
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名AI助理，你的名字叫豆包，请你用简练的语气回答用户的问题"},
        {"role": "user", "content": "你是谁，你能为我做什么"},
    ],
    stream=False
)

print(response.choices[0].message.content)