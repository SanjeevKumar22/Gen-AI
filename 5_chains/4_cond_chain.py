from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel,Field
from langchain.schema.runnable import RunnableBranch,RunnableLambda
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')

parser = PydanticOutputParser(pydantic_object=Feedback)
parser1 = StrOutputParser()

prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} {format}',
    input_variables=['feedback'],
    partial_variables={'format':parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser

prompt2 = PromptTemplate(
    template='Write an Appropriate response on positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an Appropriate response on negative feedback \n {feedback}',
    input_variables=['feedback']
)
# branch_chain = RunnableBranch(
#     (condition1,chain),(condition2,chain),default chain
# )

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive',prompt2 | model | parser1),
    (lambda x:x.sentiment == 'negative',prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain
result = chain.invoke({'feedback':"performance of the car is not good"})
print(result)
chain.get_graph().print_ascii()