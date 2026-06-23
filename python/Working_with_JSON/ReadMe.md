# Working with JSON

## What was learnt

JSON syntax methods and data types
Converting Python Dictionaries to JSON and vice versa

The act of converting data into the JSON format is referred to as serialization. 
The opposite process, deserialization, involves decoding data from the JSON format back into a usable form within Python.

The json.dump() function has two required arguments:  
The object you want to write
The file you want to write into

## Operations with code samples

Python’s json module can convert variables to data. This can come in handy when you’re using variables as dictionary keys:

dog_id = 1  
dog_name = "Frieda"  
dog_registry = {dog_id: {"name": dog_name}}  
json.dumps(dog_registry)  
'{"1": {"name": "Frieda"}}'  

Resource: https://realpython.com/python-json/
Quiz: https://realpython.com/quizzes/python-json/

