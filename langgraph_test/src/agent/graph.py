from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

llm = ChatOpenAI(
    model='qwen3-8b',
    temperature=0.8,
    api_key='xx',
    base_url="http://localhost:6006/v1",
    extra_body={'chat_template_kwargs': {'enable_thinking': False}},
)

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"今天{city}天气🌤!"

graph = create_react_agent(
    llm,
    tools=[get_weather],
    prompt="You are a helpful assistant"
)