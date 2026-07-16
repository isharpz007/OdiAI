import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

if key:
    print("API key loaded successfully.")
    print(key[:12]+"...")  # Print first and last 12 characters of the key for verification
else:
    print("Failed to load API key.")