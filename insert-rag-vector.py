# follow instructions as defined here
# but modify this for openAI
# https://docs.pinecone.io/guides/get-started/build-a-rag-chatbot

from langchain_text_splitters import MarkdownHeaderTextSplitter
from uuid import uuid4

# local imports
from ragvectorstore import ragVectorStore


data_file = "data/wondervector.md"


with open(data_file, "r") as file:
    markdown_document = file.read()

print("document:", markdown_document)


# Chunk the document based on h2 headers.
# TODO add the meta data of the file name in the documents
headers_to_split_on = [
    ("##", "Header 2")
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on, strip_headers=False
)
# these are langchain Documents split by the header markdown
# they content two properties page_content and metadata
# from langchain_core.documents import Document
# begining with ##
documents = markdown_splitter.split_text(markdown_document)

print("Total documents:", len(documents))
# Total document: 5

for doc in documents:
    print(f" content: {doc.page_content} metadata: {doc.metadata}")

'''
content: ## Introduction  
Welcome to the whimsical world of the WonderVector5000, an astonishing leap into the realms of imaginative technology. This extraordinary device, borne of creative fancy, promises to revolutionize absolutely nothing while dazzling you with its fantastical features. Whether you're a seasoned technophile or just someone looking for a bit of fun, the WonderVector5000 is sure to leave you amused and bemused in equal measure. Let's explore the incredible, albeit entirely fictitious, specifications, setup process, and troubleshooting tips for this marvel of modern nonsense.## Product overview  
The WonderVector5000 is packed with features that defy logic and physics, each designed to sound impressive while maintaining a delightful air of absurdity:- Quantum Flibberflabber Engine: The heart of the WonderVector5000, this engine operates on principles of quantum flibberflabber, a phenomenon as mysterious as it is meaningless. It's said to harness the power of improbability to function seamlessly across multiple dimensions.  
- Hyperbolic Singularity Matrix: This component compresses infinite possibilities into a singular hyperbolic state, allowing the device to predict outcomes with 0% accuracy, ensuring every use is a new adventure.  
- Aetherial Flux Capacitor: Drawing energy from the fictional aether, this flux capacitor provides unlimited power by tapping into the boundless reserves of imaginary energy fields.  
- Multi-Dimensional Holo-Interface: Interact with the WonderVector5000 through its holographic interface that projects controls and information in three-and-a-half dimensions, creating a user experience that's simultaneously futuristic and perplexing.  
- Neural Fandango Synchronizer: This advanced feature connects directly to the user's brain waves, converting your deepest thoughts into tangible actions—albeit with results that are whimsically unpredictable.  
- Chrono-Distortion Field: Manipulate time itself with the WonderVector5000's chrono-distortion field, allowing you to experience moments before they occur or revisit them in a state of temporal flux. metadata: {'Header 2': 'Introduction'}
'''

# this step is not required as default all documents are inserted with guids
# this is needed for id chunking later

uuids = [str(uuid4()) for _ in range(len(documents))]

ragVectorStore.add_documents(documents=documents, ids=uuids)

print("documents inserted")