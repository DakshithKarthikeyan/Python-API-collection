import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
response.json()
if response.status_code == 200:
    j_d = response.json()
    print(f"The joke is: {j_d['setup']} - {j_d['punchline']}")
else:
    print("Failed to retrieve joke")