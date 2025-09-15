from typing import Annotated

from langchain_core.tools import tool, BaseTool
from pydantic import BaseModel, Field


@tool
def say_hello(a:str) -> str:
    """问好：可以向输入的人名问好"""
    return f"Hello, {a}!"




@tool(return_direct=True)
def say_bye(a:Annotated[str,"这个是一个人名"]) -> str:
    """问好：可以向输入的人名拜拜"""
    return f"bye, {a}!"



print(say_hello.name)
print(say_hello.description)
print(say_hello.args)
print(say_hello.args_schema)#pytandic对象
print(say_hello.args_schema.model_json_schema())#pytandic对象转化成json对象

print(say_bye.return_direct)
print(say_hello.return_direct)

"""
def tool(name_or_callable: str | (...) -> Any | None = None,            #“名字”
         runnable: Runnable | None = None,                          
         *args: Any,
         description: str | None = None,                                #可以在函数下一行写，比如 ”“”描述“”“
         return_direct: bool = False,                                   #函数输出结果是否为一个最终结果
         args_schema: type[BaseModel] | dict[str, Any] | None = None,   #传一个pytandic对象
         infer_schema: bool = True,
         response_format: Literal["content", "content_and_artifact"] = "content",
         parse_docstring: bool = False,                                 #采用谷歌的描述格式
         error_on_invalid_docstring: bool = True) -> BaseTool | ((...) -> Any | Runnable) -> BaseTool
"""

