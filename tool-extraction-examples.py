# external imports

from typing import Optional, List

# for providing the data objects to be extracted
# there is no need to install this library
# this is present by default
from pydantic import BaseModel, Field

# providing examples to tools
from langchain_core.utils.function_calling import tool_example_to_messages

# local imports
from modelclient import modelClient

class Person(BaseModel):
    """Information about a person."""

    # ^ Doc-string for the entity Person.
    # This doc-string is sent to the LLM as the description of the schema Person,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    name: Optional[str] = Field(default=None, description="The name of the person")
    hair_color: Optional[str] = Field(
        default=None, description="The color of the person's hair if known"
    )
    height_in_meters: Optional[str] = Field(
        default=None, description="Height measured in meters"
    )

class Data(BaseModel):
    """Extracted data about people."""
    # Creates a model so that we can extract multiple entities.
    people: List[Person]  


examples = [
    (
        "The ocean is vast and blue. It's more than 20,000 feet deep.",
        Data(people=[]),
    ),
    (
        "Fiona traveled far from France to Spain.",
        Data(people=[Person(name="Fiona", height_in_meters=None, hair_color=None)]),
    ),
]

print("printing structure of examples")
print(examples);
'''
[("The ocean is vast and blue. It's more than 20,000 feet deep.", Data(people=[])), ('Fiona traveled far from France to Spain.', Data(people=[Person(name='Fiona', hair_color=None, height_in_meters=None)]))]

'''


messages = []

print("Calling the tool")
for txt, tool_call in examples:
    if tool_call.people:
        # This final message is optional for some providers
        ai_response = "Detected people."
    else:
        ai_response = "Detected no people."
    
    messages.extend(tool_example_to_messages(txt, [tool_call], ai_response=ai_response))

for message in messages:
    message.pretty_print()

'''
LangChainBetaWarning: The function `tool_example_to_messages` is in beta. It is actively being worked on, so the API may change.
  messages.extend(tool_example_to_messages(txt, [tool_call], ai_response=ai_response))
================================ Human Message =================================

The ocean is vast and blue. It's more than 20,000 feet deep.
================================== Ai Message ==================================
Tool Calls:
  Data (31e36eaf-b6a1-480b-b0be-ac10af0c9188)
 Call ID: 31e36eaf-b6a1-480b-b0be-ac10af0c9188
  Args:
    people: []
================================= Tool Message =================================

You have correctly called this tool.
================================== Ai Message ==================================

Detected no people.
================================ Human Message =================================

Fiona traveled far from France to Spain.
================================== Ai Message ==================================
Tool Calls:
  Data (9e49a0aa-b616-4ff5-9776-0dc2f5a571eb)
 Call ID: 9e49a0aa-b616-4ff5-9776-0dc2f5a571eb
  Args:
    people: [{'name': 'Fiona', 'hair_color': None, 'height_in_meters': None}]
================================= Tool Message =================================

You have correctly called this tool.
================================== Ai Message ==================================

Detected people.
'''


# Passing a message where there are no people
message_no_extraction = {
    "role": "user",
    "content": "The solar system is large, but earth has only 1 moon.",
}

structured_llm = modelClient.with_structured_output(schema=Data)
print(" LLM extracting data incorrectly")
wrong_people = structured_llm.invoke([message_no_extraction])
print(wrong_people)
'''
LLM extracting data incorrectly
people=[]

'''
print(" LLM extracting data correctly with no person")
correct_people = structured_llm.invoke(messages + [message_no_extraction])
print(correct_people)

'''
LLM extracting data correctly with no person
people=[]
'''

# This step was not required for gpt4.0 as it didn't extract person from
# the text
