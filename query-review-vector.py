# local imports
from reviewvectorstore import reviewVectorStore

# similarity search
results = reviewVectorStore.similarity_search(
    "LangChain provides abstractions to make working with LLMs easy",
    k=2,
    filter={"source": "tweet"},
)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")

'''
Response:
* Building an exciting new project with LangChain - come check it out! [{'source': 'tweet'}]
* LangGraph is the best framework for building stateful, agentic applications! [{'source': 'tweet'}]
'''

# search with score
results_score = reviewVectorStore.similarity_search_with_score(
    "Will it be hot tomorrow?", k=1, filter={"source": "news"}
)
for res, score in results_score:
    print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")

'''
Response:
* [SIM=0.569223] The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees. [{'source': 'news'}]
'''


# Query by turning into retriever
# This would directly print the results
retriever = reviewVectorStore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 1, "score_threshold": 0.4},
)
docs = retriever.invoke("Stealing from the bank is a crime", filter={"source": "news"})

# This returns a document structure
#  Document(
#     page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
#     metadata={"source": "tweet"}
for doc in docs:
    print(f" content: {doc.page_content} metadata: {doc.metadata}")

'''
Response for only doc
page_content='Robbers broke into the city bank and stole $1 million in cash.' metadata={'source': 'news'}
Response for specific
content: Robbers broke into the city bank and stole $1 million in cash. metadata: {'source': 'news'}

'''