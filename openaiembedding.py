from settings import Settings
from langchain_openai import OpenAIEmbeddings

openaiEmbeddings = OpenAIEmbeddings(model = Settings.openAI.embeddingSmall)

