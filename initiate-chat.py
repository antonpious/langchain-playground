from modelclient import modelClient
from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Spanish", "text": "hi welcome to your world of AI!"})

response = modelClient.invoke(prompt)
print(response.content)

# This should print
# ¡Hola! ¡Bienvenido a tu mundo de IA!
