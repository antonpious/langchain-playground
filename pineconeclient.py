from pinecone import Pinecone

# local imports
from settings import Settings


# The environmental variable PINECONE_API_KEY should be present
pineconeClient = Pinecone()

# This assumes that the index has already been created
# please check the repo pinecone-playground on how to create the index
pineconeIndex = pineconeClient.Index(Settings.pineCone.indexName)