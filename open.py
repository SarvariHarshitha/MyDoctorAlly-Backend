from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

client = OpenAI(api_key=api_key)

def report_gen(clean_text):
    responses = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system", 
                "content": "You are a Doctor assistant. Analyze the conversation between Doctor and Patient given as input and generate the diagnosis and prescription and required medical test for the patient as a report and format the report"
                },
            {
                'role':'user',
                'content':clean_text
            }
        ]
    )
    return responses.choices[0].message.content




if __name__ == '__main__':
    pass





