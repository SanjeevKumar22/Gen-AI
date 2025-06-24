from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
embedding.embed_query("what is genai")
# embedding.embed_documents() // use for documents