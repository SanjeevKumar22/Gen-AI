from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',temperature=0,max_tokens=10)
result = model.invoke("what is genai")
print(result.content)