import json
from difflib import get_close_matches
from dotenv import load_dotenv, dotenv_values
import os

#Environmental variables
replies = os.getenv('replies')
similarity = os.getenv('similarity')

def load_knowledge_db(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge_db(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent =2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=replies, cutoff=similarity)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_db: dict) -> str | None:
    for q in knowledge_db["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def chat_bot():
    knowledge_db: dict = load_knowledge_db('knowledge_db.json')

    print('------------------------------------------ \n')
    print('Welcome to my project! \n')
    print('You can find me in GitHub -> https://github.com/LuterDEV')
    print('In Linkedin -> https://www.linkedin.com/in/martin-ojeda-alonso/')
    print('In Instagram -> https://www.instagram.com/luteeeeeer/')
    print('Or in Twitch -> ******* \n')
    print('------------------------------------------ \n')
    

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'bye':
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_db["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_db)
            print(f'Bot: {answer}') # type: ignore

        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_db["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_db('knowledge_db.json', knowledge_db)
                print('Bot: Thank you! I learned a new response!')
        