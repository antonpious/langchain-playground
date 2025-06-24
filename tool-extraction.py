from typing import Optional

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
    

person_data = {
                    'name': 'Andrew Smith', 
                    'hair_color': 'blonde',
                    'height_in_meters': '6ft 2 inches'
                 }


# unpack the dictionary before passing
# * for list, tuple and set ** for dictionary
andrew = Person(**person_data)

# verify the object is set
print(andrew)

# access the property directly
print(andrew.hair_color)

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
structured_llm = modelClient.with_structured_output(schema=Person)

# test the extraction
text = "Alan Smith is 6 feet tall and has blond hair."
prompt = prompt_template.invoke({"text": text})

# this return the person object
person = structured_llm.invoke(prompt)

print(person)

print(f"name:{person.name} height_in_meters:{person.height_in_meters}")
'''
name='Alan Smith' hair_color='blond' height_in_meters='1.83'
name:Alan Smith height_in_meters:1.83
note the conversion of feet to meters
'''

# what happens if there are two names
text2 = "Mary Jane is 5 feet 5 inches tall and has blond hair. Peter Parker is 6 feet 2 inches tall and has brown hair"
prompt2 = prompt_template.invoke({"text": text2})

# this return the person object
person2 = structured_llm.invoke(prompt2)

print(person2)
# This extracts only the first one
print(f"name:{person2.name} height_in_meters:{person2.height_in_meters}")

'''
name='Mary Jane' hair_color='blond' height_in_meters='1.65'
name:Mary Jane height_in_meters:1.65
'''