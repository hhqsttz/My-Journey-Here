from langchain_core.messages import AIMessage
from langchain_core.output_parsers import PydanticOutputParser

a = AIMessage(content="你好")
print(a)
PydanticOutputParser()