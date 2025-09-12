from langchain_openai import ChatOpenAI
from llm_instance_creation.env_test import OPENAI_BASE_URL, OPENAI_API_KEY, BASE_URL, BASE_API_KEY

llm= ChatOpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY,
    model="llm.name",
    temperature=0.8
)
LOCAL_llm= ChatOpenAI(
    base_url=BASE_URL,
    api_key=BASE_API_KEY,
    model="LOCAL_llm.name",
    temperature=0.8
)