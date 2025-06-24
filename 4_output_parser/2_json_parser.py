from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = JsonOutputParser()

template1 = PromptTemplate(
    template='Give a name, age , city of a person \n {format}',
    input_variables=[],
    partial_variables={'format':parser.get_format_instructions()}
)

prompt = template1.format()

result = model.invoke(prompt)

final = parser.parse(result.content)
print(final)

chain = template1 | model | parser

result = chain.invoke({})
print(result)