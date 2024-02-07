import requests

# num = int(input("number of questions: "))

params = {
    "amount": 10,
    "type": "boolean"
}

request = requests.get("https://opentdb.com/api.php", params=params)
data = request.json()

question_data = data['results']
