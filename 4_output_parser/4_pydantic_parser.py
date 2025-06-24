from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

class schema (BaseModel):
    name: str = Field(description='name of a person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=schema)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format}',
    input_variables=[],
    partial_variables={'format':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place': 'us'})

print (result)