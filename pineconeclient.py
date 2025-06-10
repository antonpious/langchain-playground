from pinecone import Pinecone
from settings import Settings

pineconeClient = Pinecone()

pineconeIndex = pineconeClient.Index(Settings.pineCone.indexName)