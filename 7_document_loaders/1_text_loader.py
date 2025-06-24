from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
prompt = PromptTemplate(
    template='Write a summary of the poem \n. {poem}',
    input_variables=['poem']
)

loader = TextLoader('sample.txt',encoding='utf-8')

docs = loader.load()
parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({'poem':docs[0].page_content})
print(result)