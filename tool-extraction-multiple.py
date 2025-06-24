from typing import Optional, List

# for providing the data objects to be extracted
# there is no need to install this library
# this is present by default
from pydantic import BaseModel, Field

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

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




person1 = {
                    'name': 'Andrew Smith', 
                    'hair_color': 'black',
                    'height_in_meters': '6ft 2 inches'
                 }

person2 = {
                    'name': 'Mary Jane', 
                    'hair_color': 'blonde',
                    'height_in_meters': '5ft 6 inches'
                 }

andrew = Person(**person1)
mary = Person(**person2)

persons = [andrew, mary]

members = Data(people=persons)


print(members)

for person in members.people:
    print("printing person")
    print(person)

# verify the object is set


# initial the llm calls.
# Define a custom prompt to provide instructions and any additional context.
# 1) You can add examples into the prompt template to improve extraction quality
# 2) Introduce additional parameters to take context into account (e.g., include metadata
#    about the document from which the text was extracted.)
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "If you do not know the value of an attribute asked to extract, "
            "return null for the attribute's value.",
        ),
        # Please see the how-to about improving performance with
        # reference examples.
        # MessagesPlaceholder('examples'),
        ("human", "{text}"),
    ]
)

# provide the structure to extract data from
# this time we give the collection
structured_llm = modelClient.with_structured_output(schema=Data)


text = "My name is Jeff, my hair is black and i am 6 feet tall. Anna has the same color hair as me and is 2 inches taller than me."
prompt = prompt_template.invoke({"text": text})
people = structured_llm.invoke(prompt)
print(people)

'''
people=[
    Person(name='Jeff', hair_color='black', height_in_meters='1.83'), 
    Person(name='Anna', hair_color='black', height_in_meters='1.88')
    ]
'''