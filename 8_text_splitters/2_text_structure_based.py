from langchain.text_splitter import RecursiveCharacterTextSplitter


text = """
dfsaaaaaaaaaaaaaaaaasafsafdadsadasssssssssssssssssdas
sadasdsadasdasdasssssssssssssssssasdasda

asddadasdsaaaaaaaaaaaaaaaaasdada
sdasdsadsadasd

"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

result = splitter.split_text(text)
print(result)