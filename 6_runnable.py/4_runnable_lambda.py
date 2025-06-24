from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableLambda,RunnableParallel,RunnableSequence,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count':RunnableLambda(lambda x:len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
result = final_chain.invoke({'topic':"AI"})
print(result)
final_chain.get_graph().print_ascii()