from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from pydantic.v1 import BaseModel
from llm_instance_creation.llm_model import llm

prompt1 = PromptTemplate.from_template("这是一个基础提示词模板，可以传一个{input}")

prompt = ChatPromptTemplate.from_messages([
    ("system","你是一个乐于助人人的机器人，通过上下文历史记录，尽你所能回答问题"),
    #message的三种方式
    ("user","{input}"),  #双元组
    {"role":"ai","content":"你好，亲爱的用户"}, #openai式的message
    MessagesPlaceholder(variable_name="chat_history",optional=True)#消息占位符（optional可选信息，可有可无）
])

chain=prompt1 | llm

res=chain.invoke({"input":"你好，你是谁？"})

#三种输出方式
#1.输出解释器
chain1=prompt | llm | JsonOutputParser
#2.结构化输出,绑定llm
runnable2 = llm.with_structured_output(BaseModel) #参数接一个pytandic类
chain2=runnable2 | prompt
#3.绑定工具,本质上也是第二种
runnable3 = llm.bind_tools([BaseModel]) #参数接一个pytandic类





