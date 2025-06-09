from dotenv import load_dotenv 
import json
from box import Box


# This file is to be loaded for all modules
# loading the environmental variables from .env file
load_dotenv() 

# Box provides a clean dot syntax available to other languages
# Currently this is not available during typing
# Todo how to make the object available during code writing

def load_settings(file_name):
        try:
            with open(file_name, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("File not found:", file_name)
        except Exception as ex:
            print("Generic", ex)


def loadSettings():
    settings_file = "settings.json"
    print("loading settings")
    settings_data = load_settings(settings_file)
    settings_object = Box(settings_data)
    return settings_object



'''
Python by default executes the function
only once.
so there is no need to check for empty

def loadConstants():
    constants_file = "constants.json"
    constants_object = None
    if constants_object:
        print("do nothing give back constants")
    else:
        print("loading constants")
        constants_data = load_settings(constants_file)
        # print("Json Data",constants_data)
        constants_object = Box(constants_data)
    return constants_object
'''
    

Settings = loadSettings()


# error logging syntax
# https://raphealenike.medium.com/a-comprehensive-guide-for-understanding-errors-and-exception-handling-in-python-8b6e3a2c5d5c