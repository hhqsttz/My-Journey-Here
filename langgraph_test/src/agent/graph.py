from typing import List

from anyio.lowlevel import checkpoint
from langchain_core.messages import SystemMessage, AnyMessage, AIMessage
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from langgraph.graph import message
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState
from langgraph_runtime_inmem.checkpoint import InMemorySaver

llm = ChatOpenAI(
    model='qwen3-8b',
    temperature=0.8,
    api_key='xx',
    base_url="http://localhost:6006/v1",
    extra_body={'chat_template_kwargs': {'enable_thinking': False}},
)
def prompt (config:RunnableConfig,state:AgentState) ->List[AnyMessage]:
    user_name = config["configurable"].get("user_name","zs")

    s_message = f"系统提示词，{user_name}"

    return [{"role":"system","content":s_message}]+state["messages"]


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"今天{city}天气🌤!"
checkpointer = InMemorySaver()

graph = create_react_agent(
    llm,
    tools=[get_weather],
    prompt = prompt     #动态设定提示词
)
# from langgraph_sdk import get_sync_client
#
# client = get_sync_client(url="http://localhost:2024") #Rustfulapi接口
#
# for chunk in client.runs.stream(
#     None,                                                          # Threadless run 是否启用一个线程
#     "agent", # Name of assistant. Defined in langgraph.json.
#     input={"messages": [{"role": "human","content": "What is LangGraph?",}],},
#     stream_mode="messages-tuple",                                  #消息一个一个token流式输出
#     config={"configurable":{"user_name":"name","threa_id":1}},                  #测试的时候这里传一个config
#     checkpointer=checkpointer                                        #设置存储检查点
#    ):
#
#     print(f"Receiving new event of type: {chunk.event}...")
#     print(chunk.data)
#     print("\n\n")
