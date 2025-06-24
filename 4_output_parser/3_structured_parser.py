from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

schema = [
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template1 = PromptTemplate(
    template='Give a name, age , city of a person \n {format}',
    input_variables=[],
    partial_variables={'format':parser.get_format_instructions()}
)

chain = template1 | model | parser
result = chain.invoke({})
print(result)
