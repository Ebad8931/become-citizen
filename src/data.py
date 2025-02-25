import json
import os
from random import choice

from app_constants import data_dir

def get_phrase() -> str:
    
    phrases_data_path = os.path.join(data_dir, 'phrases.json')

    with open(phrases_data_path, "r") as file:
        sentences = json.load(file)

    return choice(sentences)


def get_question() -> dict:
    
    questions_data_path = os.path.join(data_dir, 'questions.json')
    
    with open(questions_data_path, "r") as file:
        questions = json.load(file)

    return choice(questions)


if __name__ == "__main__":
    print(get_question())
    print(get_phrase())