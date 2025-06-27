from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


text = "asdasodjasiodjasijdaodjaofsbvsvbsifhscbsiodfhsadfhsadhhhhhhhhhhhhhhhhhjhfsoiefh"
splitter = CharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)
print(result)

loader = PyPDFLoader(file_path=r'D:\Coding\GenAI\7_document_loaders\pdf\Marchio Trek.pdf')
docs = loader.load()

result = splitter.split_documents(docs)
print(result)
