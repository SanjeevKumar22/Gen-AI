from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(file_path=r"d:\Coding\GenAI\7_document_loaders\kashmir.pdf")
docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)