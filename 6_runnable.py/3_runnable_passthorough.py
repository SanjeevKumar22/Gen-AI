from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv  import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
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

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt1,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({'topic':'AI'})
print(result)