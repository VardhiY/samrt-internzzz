from dotenv import load_dotenv
import openai
import os

load_dotenv()  # loads .env file from the current directory

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code_from_text(prompt: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes clean Python code."},
                {"role": "user", "content": f"Write Python code for: {prompt}"}
            ],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"# Error generating code: {str(e)}"
