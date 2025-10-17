import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Check if the API key is loaded
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")
print("✅ API Key loaded, environment configured successfully.")

try:
    # 3. Configure the Gemini API
    genai.configure(api_key=api_key)
    print("✅ Gemini API configured successfully.") 

    #4. Test the connection by making a simple request
    print("⏳ Testing connection to Gemini API...")
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content("Hello, Gemini!")

    #5. Print the response from the API
    print("✅ Connection successful. Response from Gemini API:")
    print("LLM Response", response.text)     

except  Exception as e:
    print(f"Error Connecting to Gemini API:{e} ")

