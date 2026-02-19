import requests

def print_three_cat_facts():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    print(data["fact"])
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    print(data["fact"])
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    print(data["fact"])
print_three_cat_facts()
