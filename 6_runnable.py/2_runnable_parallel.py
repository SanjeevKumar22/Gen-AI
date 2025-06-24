from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv  import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

prompt = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt1 = PromptTemplate(
    template="generate a linkedin post about {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedin': RunnableSequence(prompt1,model,parser)
})


result = parallel_chain.invoke({'topic':'AI'})

print(result)