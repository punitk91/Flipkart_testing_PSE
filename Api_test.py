import json
import requests
import re

# Task 1 --- > " https://jsonplaceholder.typicode.com/posts "

response = requests.get("https://jsonplaceholder.typicode.com/posts","\\n")
json_data = json.loads(response.text )
print(json.dumps(json_data, indent = 1)) # Printing data with format


# Task 2 ---- >  https://jsonplaceholder.typicode.com/posts/1/comments

response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
json_data = json.loads(response.text)
dict = {}

# Regex expression
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
for subVal in json_data:
    # Check weather it is valid or not
    if (re.match(regex, subVal["email"])):

        if subVal["postId"]  in dict:
            dict[subVal["postId"]].append(subVal["email"])
        else:
            dict[subVal["postId"]] = [subVal["postId"]]
print (dict)


