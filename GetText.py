import requests
import random


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def get():
    try:
        response = requests.get(url='https://api.quotable.io/random').json()
        response = response['content']
    except:
        response = load_text()
    return response
