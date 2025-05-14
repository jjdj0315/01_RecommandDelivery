import os

import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

KEYWORDS_BLACKLIST = ['리뷰', 'zㅣ쀼', 'ZI쀼', 'Zl쀼', '리쀼', '찜', '이벤트', '추가', '소스']
KEYWORDS_CONTEXT = [
    '해장', '숙취',
    '다이어트'
]

def get_embedding(text, model = 'text-embedding-3-small'):
    clint = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    respone = clint.embeddings.create(
        input = text,
        model = model
    )
    return respone.data[0].embedding

def get_embeddings(text, model = 'text-embedding-3-small'):
    clint = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    responese = clint.embeddings.create(
        input=text,
        model = model
    )
    output = []
    for i in range(len(responese.data)):
        output.append(responese.data[i].embedding)
    return output

