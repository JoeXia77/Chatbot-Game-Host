

import openai
import json

openai.api_key = "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"

json_path = "./Story1.json"
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

    question = data["question"]
    truth = data["truth"]


prompt = f"""
Translate the following two Chinese texts in angle bracket into English.
Chinese texts 1: 
Question: <{question}>
Chinese texts 2: 
Truth: <{truth}>
Then output a json file using question and truth as key, the translated english text as content:

"""

print(prompt)

messages = [{"role": "user", "content": f'{prompt}'}]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
    max_tokens=1000,
)
response_content_str = response['choices'][0]['message']['content']
response_content = json.loads(response_content_str)
print(response_content)

## save it to json file
json_path = "./Story1_eng.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(response_content, f, ensure_ascii=False, indent=4)




















