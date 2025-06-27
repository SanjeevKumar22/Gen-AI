from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """
def className:
    print "hi"

class A:
    a=10
    b=10    

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=10,
    chunk_overlap=0,
    language=Language.PYTHON
)

result = splitter.split_text(text)
print(result)