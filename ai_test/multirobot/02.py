
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory

from llm_instance_creation.llm_model import llm

prompt3 = ChatPromptTemplate.from_messages([
    ("system", "你是一个乐于助人人的机器人，通过上下文历史记录，尽你所能回答问题"),
    # message的三种方式
    MessagesPlaceholder(variable_name="chat_history", optional=True),  # 消息占位符（optional可选信息，可有可无）
    ("user", "{input}"),  # 双元组
    # {"role": "ai", "content": "你好，亲爱的用户"}  openai式的message

])

chain3 = prompt3 | llm

# 保存历史聊天记录案例

# 1.存入内存当中，进程结束就消失
# store = {}用来存{"session_id":ChatMessageHistory对象}
# ChatMessageHistory对象的核心属性
# messages: list[BaseMessage] = Field(default_factory=list)
# a = ChatMessageHistory()
# 方法名	作用描述	参数说明
# add_message(message)	添加一个 BaseMessage 对象到历史记录中。	message: 一个 BaseMessage 或其子类的实例。
# add_user_message(message)	添加一条用户消息到历史记录中。	message: 字符串，用户消息的文本内容。
# add_ai_message(message)	添加一条AI消息到历史记录中。	message: 字符串，AI消息的文本内容。
# clear()	清空所有的聊天消息，将 messages 列表置空。	无参数。
# a.messages=[BaseMessage]=[SystemMessage(content="内容"),AIMessage(content="内容"),HumanMessage(content="内容"),ToolMessage(content="内容")]
# 消息对象有两种属性  a=SystemMessage(content="内容") a.type = "system",a.content="内容"
store = {}
def get_session_history1(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
#2.存入关系型数据库
def get_session_history2(session_id: str):
    return SQLChatMessageHistory(
        session_id=session_id,
        connection_string="sqlite:///:memory:" #SQLAIChemy的url地址
    )
#3.对历史消息进行汇总，保留两条最新的消息。
def summarize_messages(current_input):
    session_id = current_input["config"]["configurable"]["session_id"]
    if not session_id :
        return False
    history = get_session_history1(session_id)
    if len(history.messages) <= 2 :
        return False
    chat_history =  history.messages[:-2]
    summary_history = history.messages[-2:]
    p =ChatPromptTemplate([
        ("system","请将下列历史消息总结成摘要，来进行用户回答"),
        ("placeholder","{chat_history}"),
        ("human","请保留重要事实和决策")
    ])

    c = p | llm
    history.clear()
    history.add_message(c.invoke({"chat_history":chat_history}))
    for i in summary_history:
        history.add_message(i)
    return True
#4创建带有处理历史功能的链
chain_with_history1 = RunnableWithMessageHistory(
    chain3,
    get_session_history1,
    input_messages_key="intput",
    history_messages_key="chat_history"
)
chain_with_history2 = RunnableWithMessageHistory(
    chain3,
    get_session_history2,
    input_messages_key="intput",
    history_messages_key="chat_history"
)

res = chain_with_history1.invoke({"input": "你是谁？"},config = {"configurable": {"session_id": "你的会话ID"}})

