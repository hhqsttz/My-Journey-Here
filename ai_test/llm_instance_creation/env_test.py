import os

from dotenv import load_dotenv

##在.env文件加载所需的env
load_dotenv(verbose=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

BASE_URL = os.getenv("BASE_URL")
BASE_API_KEY = os.getenv("BASE_API_KEY")