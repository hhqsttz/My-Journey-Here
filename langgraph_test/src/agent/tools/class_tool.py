from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import StructuredTool, BaseTool
from pydantic import BaseModel, Field



class class_tool1(BaseTool):
    name:str="class_tool1",
    args_schema:BaseModel = None,
    description:str = "这是一个chain转为的工具",
    def func1(self):
        pass
