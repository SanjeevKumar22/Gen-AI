from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

template1 = PromptTemplate(
    template='write a detailed report of {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 lines summary report for below text.\n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke('black hole')

result = model.invoke(prompt1)


prompt2 = template2.invoke(result.content)

result1 = model.invoke(prompt2)
