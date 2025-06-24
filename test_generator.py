from dotenv import load_dotenv
import openai
import os

load_dotenv()  # loads .env file from the current directory

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tests_from_code(code: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert Python developer. Generate unit tests for the provided code."},
                {"role": "user", "content": f"Write Python unit test cases for this code:\n\n{code}"}
            ],
            temperature=0.3,
            max_tokens=500,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"# Error generating test cases: {str(e)}"
