from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


#将函数转化为一个Runnable对象
#同步
def say_hello_T(a) -> str:
    return f"Hello, {a}!"
#异步
async def say_hello_Y(a) -> str:
    return f"Hello, {a}!"

class name (BaseModel):
    a: str = Field(description="人名")
#1.函数转工具
say_hello = StructuredTool(
    name="say_hello",
    description="这个是一个向输入的人问好的工具",
    args_schema=name,
    func=say_hello_T,
    coroutine=say_hello_Y,


    )
#2.langchain的链转为工具
a = PromptTemplate.from_template("什么也不用做")
chain = a | JsonOutputParser
T = chain.as_tool(
    name="这是一个chain转为的工具",
    args_schema = None,
    description = None,
    arg_types= None
)
