import json
import os
from llamaapi import LlamaAPI

# Initialize the SDK
llama = LlamaAPI("LL-zN9kfuCx4vxGUw7qWVQlMpI8vSwjErPcH9zxz3dkVBQim2SrSQP2F4WKJ3SlYZ9y")

k = 100     # lenght of the summary
n = 5       # N times to do summarization

description = "Summarize this text in "+str(k)+" words: "


def summarize(text, desc):
    # Build the API request
    api_request_json = {
        'model': 'llama-13b-chat',
        'messages': [
            {'role': 'user', 'content': desc + text}],
    }

    # Execute the Request
    response = llama.run(api_request_json)
    # print(json.dumps(response.json(), indent=2))

    response_data = response.json()

    # Extract the text argument
    text_argument = response_data['choices'][0]['message']['content']

    # Print the extracted text argument
    # print(x)
    return text_argument

text = [None] * 10

for i in range(5):
    print("--------------------------------------------------------------------")
    print(f"file{i}.txt")

    file_path = os.path.join("./texts", f"text{i}.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    text[i] = summarize(content, description)

    print("--------------------------------------------------------------------")

try:
    file_path = "output.txt"
    with open(file_path, "w", encoding="utf-8") as file:        
        for i in range(5):
            file.write(text[i])
except Exception as e:
    print(f"Unexpected error: {e}")

summary = [None] * 5

file_path = os.path.join("output.txt")
with open(file_path, "r", encoding="utf-8") as file:
    summary[0] = file.read()

try:
    file_path = "summary.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for i in range(1,n+1):
            summary[i] = summarize(summary[i-1], "Summarize this text: ")        
            file.write("Summary "+str(i)+":\n"+summary[i]+"\n\n")
except Exception as e:
    print(f"Unexpected error: {e}")
        
