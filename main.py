import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
args = sys.argv[1:]

if not args: # args is empty in this case, so it is "falsy" in python
    print("No prompt was provided. Please provide prompt.")
    sys.exit(1)

user_prompt = sys.argv[1]

flags = None
if sys.argv[2:]:
    flags = sys.argv[2]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)

if flags == "--verbose":
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)

