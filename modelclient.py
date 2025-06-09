import os
from dotenv import load_dotenv 
from langchain.chat_models import init_chat_model

# loading variables from .env file
load_dotenv() 

# there is no need to get the key
# the key is expected to be in the environmental variables
# os.getenv("OPENAI_API_KEY")

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4o-mini", model_provider="openai")



openaiClient = openai
