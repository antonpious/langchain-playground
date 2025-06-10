
# RAG vector store stored in namespace tenant3
from langchain_pinecone import PineconeVectorStore

# Local imports
from settings import Settings
from pineconeclient import pineconeIndex
from openaiembedding import openaiEmbeddings

ragVectorStore = PineconeVectorStore(
    index = pineconeIndex, 
    embedding = openaiEmbeddings, 
    namespace = Settings.pineCone.ragNamespace)