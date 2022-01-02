import json
import random


def getSnippet(choice):
    snippets = json.load(open("snippets.json"))
    return random.choice(snippets[choice])
