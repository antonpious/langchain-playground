from settings import Settings
from langchain.chat_models import init_chat_model

# command + / for uncommenting this block
# import os
# #the openAI API key is expected to be in the environmental variables
# print(os.getenv("OPENAI_API_KEY"))


# initialize the model
modelClient = init_chat_model(Settings.openAI.mini, 
                              model_provider=Settings.openAI.provider)






