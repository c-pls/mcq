import json
from random import randint
import time

def load_question(filename):
    """
    Load the questions from JSON file into Python Dictionary
    """
    with open(filename, 'r') as read_file:
        questions = json.load(read_file)
    return questions

