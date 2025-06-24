from dotenv import load_dotenv
import openai
import os

load_dotenv()  # loads .env file from the current directory

openai.api_key = os.getenv("OPENAI_API_KEY")

def fix_code_bugs(code: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert Python developer. Fix bugs in the user's code."},
                {"role": "user", "content": f"Fix this code:\n{code}"}
            ],
            temperature=0.3,
            max_tokens=500,
            timeout=10
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"# Error fixing code: {str(e)}"
