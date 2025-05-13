import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "surface": 45,
    "chambres": 2,
    "quartier": "centre"
}
response = requests.post(url, json=data)
print(response.json())