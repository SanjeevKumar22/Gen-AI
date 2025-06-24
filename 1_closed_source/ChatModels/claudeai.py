from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
result=llm.invoke("what is genai")
print(result.content)