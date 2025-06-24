from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation length: {length_input}
""",
input_variables=['paper_input','style_input','length_input'],
validate_template=True
)

template.save('template.json')