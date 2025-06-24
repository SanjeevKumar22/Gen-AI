from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_path='https://www.flipkart.com/')

docs = loader.load()
print(docs)