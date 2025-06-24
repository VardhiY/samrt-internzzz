import openai
import os
from dotenv import load_dotenv

load_dotenv()  # 👈 loads your .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_code(code: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Python expert. Summarize what this code does clearly.",
                },
                {
                    "role": "user",
                    "content": code,
                },
            ],
            temperature=0.3,
            max_tokens=300,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"# Error summarizing code: {str(e)}"
