from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

chat_template = ChatPromptTemplate([
        ('system','You are helpful customer support agent'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human','{query}')
    ]
)

user_input = input('You: ')


chat_history = []

with open('D:\Coding\GenAI\prompts\chat_history.txt') as f:
    chat_history.extend(f.readlines())

# prompt = chat_template.invoke({
#     'query': user_input,
#     'chat_history': chat_history
#     })
chain = chat_template | model
result = chain.invoke({
'chat_history': chat_history,
'query': user_input
})
print(result.content)