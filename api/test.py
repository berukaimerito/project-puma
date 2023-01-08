import json
import requests
import autopep8

endpoint_url = "http://127.0.0.1:5000/scripts/ETHUSDT/run"

with open('api/user_scripts/mbappe_ETHUSDT.py') as f:
    code = f.read()
    stripped_string = code.strip()
    cleaned_string = stripped_string.replace("\n", " ")
    formatted_code = autopep8.fix_code(code, options={"max_line_length": 80, "indent_size": 2})


data  = {
    "symbol": "ETHUSDT",
    "code": cleaned_string
}

response = requests.post(endpoint_url, json=data)
# Send the POST request with the JSON payload

# Print the response status code
print(response.status_code,response.json())
