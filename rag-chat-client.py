from modelclient import modelClient

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub

# local imports
from ragvectorstore import ragVectorStore

query1 = "What are the first 3 steps for getting started with the WonderVector5000?"

answer1_without_knowledge = modelClient.invoke(query1)

print("Query 1:", query1)
print("Answer without knowledge:", answer1_without_knowledge.content)
'''
Query 1: What are the first 3 steps for getting started with the WonderVector5000?
Answer without knowledge: To get started with the WonderVector5000, you can follow these initial steps:

1. **Unbox and Inspect**: Carefully remove the WonderVector5000 from its packaging. Check for any visible damage and ensure all parts and accessories (like cables, manuals, and additional components) are included.

2. **Read the Manual**: Before setting up the device, take some time to read the user manual. This will give you a better understanding of the device's features, setup procedures, and safety precautions.

3. **Set Up Power and Connectivity**: Plug in the WonderVector5000 and turn it on. Follow the instructions for connecting it to your power source or network, depending on the model's requirements. This may include connecting it to Wi-Fi or linking it with other devices, if applicable.

After completing these steps, you’ll be ready to move on to configuration and usage.
'''


# Create the chain for retrieval
retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
retriever = ragVectorStore.as_retriever()


combine_docs_chain = create_stuff_documents_chain(
    modelClient, retrieval_qa_chat_prompt
)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)


answer1_with_knowledge = retrieval_chain.invoke({"input": query1})

print("Query 1:", query1)
print("Answer with knowledge:", answer1_with_knowledge['answer'])
print("\n")
print("Context Used:", answer1_with_knowledge['context'])

'''
Query 1: What are the first 3 steps for getting started with the WonderVector5000?
Answer with knowledge: The first three steps for getting started with the WonderVector5000 are:

1. Unpack the Device: Remove the WonderVector5000 from its anti-gravitational packaging, ensuring to handle with care to avoid disturbing the delicate balance of its components.

2. Initiate the Quantum Flibberflabber Engine: Locate the translucent lever marked “QFE Start” and pull it gently. You should notice a slight shimmer in the air as the engine engages, indicating that quantum flibberflabber is in effect.

3. Calibrate the Hyperbolic Singularity Matrix: Turn the dials labeled 'Infinity A' and 'Infinity B' until the matrix stabilizes. You'll know it's calibrated correctly when the display shows a single, stable “∞”.


Context Used: [Document(id='c6af53b7-9d7e-4b63-a834-ca1b4540fc99', metadata={'Header 2': 'Getting started'}, page_content="## Getting started  \nSetting up your WonderVector5000 is both simple and absurdly intricate. Follow these steps to unleash the full potential of your new device:  \n1. Unpack the Device: Remove the WonderVector5000 from its anti-gravitational packaging, ensuring to handle with care to avoid disturbing the delicate balance of its components.  \n2. Initiate the Quantum Flibberflabber Engine: Locate the translucent lever marked “QFE Start” and pull it gently. You should notice a slight shimmer in the air as the engine engages, indicating that quantum flibberflabber is in effect.  \n3. Calibrate the Hyperbolic Singularity Matrix: Turn the dials labeled 'Infinity A' and 'Infinity B' until the matrix stabilizes. You'll know it's calibrated correctly when the display shows a single, stable “∞”.  \n4. Engage the Aetherial Flux Capacitor: Insert the EtherKey into the designated slot and turn it clockwise. A faint humming sound should confirm that the aetherial flux capacitor is active.  \n5. Activate the Multi-Dimensional Holo-Interface: Press the button resembling a floating question mark to activate the holo-interface. The controls should materialize before your eyes, slightly out of phase with reality.  \n6. Synchronize the Neural Fandango Synchronizer: Place the neural headband on your forehead and think of the word “Wonder”. The device will sync with your thoughts, a process that should take just a few moments.  \n7. Set the Chrono-Distortion Field: Use the temporal sliders to adjust the time settings. Recommended presets include “Past”, “Present”, and “Future”, though feel free to explore other, more abstract temporal states."), Document(id='cf3b79c1-0492-4362-8b8a-e60e21d2b028', metadata={'Header 2': 'Introduction'}, page_content="## Introduction  \nWelcome to the whimsical world of the WonderVector5000, an astonishing leap into the realms of imaginative technology. This extraordinary device, borne of creative fancy, promises to revolutionize absolutely nothing while dazzling you with its fantastical features. Whether you're a seasoned technophile or just someone looking for a bit of fun, the WonderVector5000 is sure to leave you amused and bemused in equal measure. Let's explore the incredible, albeit entirely fictitious, specifications, setup process, and troubleshooting tips for this marvel of modern nonsense."), Document(id='beb0ef1c-ac47-4ca9-ade3-5b3696748417', metadata={'Header 2': 'Product overview'}, page_content="## Product overview  \nThe WonderVector5000 is packed with features that defy logic and physics, each designed to sound impressive while maintaining a delightful air of absurdity:- Quantum Flibberflabber Engine: The heart of the WonderVector5000, this engine operates on principles of quantum flibberflabber, a phenomenon as mysterious as it is meaningless. It's said to harness the power of improbability to function seamlessly across multiple dimensions.  \n- Hyperbolic Singularity Matrix: This component compresses infinite possibilities into a singular hyperbolic state, allowing the device to predict outcomes with 0% accuracy, ensuring every use is a new adventure.  \n- Aetherial Flux Capacitor: Drawing energy from the fictional aether, this flux capacitor provides unlimited power by tapping into the boundless reserves of imaginary energy fields.  \n- Multi-Dimensional Holo-Interface: Interact with the WonderVector5000 through its holographic interface that projects controls and information in three-and-a-half dimensions, creating a user experience that's simultaneously futuristic and perplexing.  \n- Neural Fandango Synchronizer: This advanced feature connects directly to the user's brain waves, converting your deepest thoughts into tangible actions—albeit with results that are whimsically unpredictable.  \n- Chrono-Distortion Field: Manipulate time itself with the WonderVector5000's chrono-distortion field, allowing you to experience moments before they occur or revisit them in a state of temporal flux."), Document(id='3b32534c-d066-4775-a292-3e2e733c18ca', metadata={'Header 2': 'Troubleshooting'}, page_content="## Troubleshooting  \nEven a device as fantastically designed as the WonderVector5000 can encounter problems. Here are some common issues and their solutions:  \n- Issue: The Quantum Flibberflabber Engine won't start.  \n- Solution: Ensure the anti-gravitational packaging has been completely removed. Check for any residual shards of improbability that might be obstructing the engine.  \n- Issue: The Hyperbolic Singularity Matrix displays “∞∞”.  \n- Solution: This indicates a hyper-infinite loop. Reset the dials to zero and then adjust them slowly until the display shows a single, stable infinity symbol.  \n- Issue: The Aetherial Flux Capacitor isn't engaging.  \n- Solution: Verify that the EtherKey is properly inserted and genuine. Counterfeit EtherKeys can often cause malfunctions. Replace with an authenticated EtherKey if necessary.  \n- Issue: The Multi-Dimensional Holo-Interface shows garbled projections.  \n- Solution: Realign the temporal resonators by tapping the holographic screen three times in quick succession. This should stabilize the projections.  \n- Issue: The Neural Fandango Synchronizer causes headaches.  \n- Solution: Ensure the headband is properly positioned and not too tight. Relax and focus on simple, calming thoughts to ease the synchronization process.  \n- Issue: The Chrono-Distortion Field is stuck in the past.  \n- Solution: Increase the temporal flux by 5%. If this fails, perform a hard reset by holding down the “Future” slider for ten seconds.")]
'''