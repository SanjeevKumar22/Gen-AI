from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path=r'D:\Coding\GenAI\7_document_loaders\pdf',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(len(docs))
print(docs[4].metadata)