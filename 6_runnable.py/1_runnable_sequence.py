from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv  import load_dotenv
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

prompt = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

result = chain.invoke({'topic':'AI'})

prompt2 = PromptTemplate(template="explain the following joke - {text}",input_variables=['text'])

chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)

result = chain.invoke({'topic':'AI'})

print(result)