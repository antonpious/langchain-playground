from langchain_pinecone import PineconeVectorStore
from settings import Settings
from pineconeclient import pineconeIndex
from openaiembedding import openaiEmbeddings

reviewVectorStore = PineconeVectorStore(
    index = pineconeIndex, 
    embedding = openaiEmbeddings, 
    namespace = Settings.pineCone.reviewNamespace)