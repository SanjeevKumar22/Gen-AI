from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt1 = PromptTemplate(
    template='Generate a 5 lines summary from the following the text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

chain = prompt | model | parser | prompt1 | model | parser

result = chain.invoke({'topic':'genai'})

print(result)
chain.get_graph().print_ascii()