"""
    four functions in json
    1. dumps(): This function is used to convert Python object to JSON string.
    2. dump(): This function is used to write JSON object to a file.
    3. loads(): This function is used to convert JSON string to Python object.
    4. load(): This function is used to load JSON object from a file.
"""

import json
from pprint import pprint

     
def json_dumps():
    """ Python program to convert Python to JSON """
    # Data to be written 
    dictionary ={ 
    "id": "04", 
    "name": "sunil", 
    "department": "HR",
    "int number": 123,
    "float number": 123.456,
    "boolean": True,
    } 
        
    # Serializing json  
    json_object = json.dumps(dictionary, indent=4) 
    print(json_object)
    print(type(json_object))

def json_dump():
    """ Python program to write JSON to a file """
    # Data to be written
    dictionary ={
        "name" : "sathiyajith",
        "rollno" : 56,
        "cgpa" : 8.6,
        "phonenumber" : "9976770500"
    }
    
    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)

def json_loads():
    """ Python program to convert JSON to Python """
    # JSON string
    json_string = '{"id": 1, "name": "sunil", "department": "HR", "int number": 123, "float number": 123.456, "boolean": true}'
    
    # Convert json to dict
    dictionary = json.loads(json_string)
    pprint(dictionary)
    print(type(dictionary))

def json_load():
    """ Python program to read JSON from a file """
    with open('sample.json', 'r') as f:
        dictionary = json.load(f)
        pprint(dictionary)
        print(type(dictionary))

    
if __name__ == "__main__":
    json_dumps()
    json_dump()
    json_loads()
    json_load()
