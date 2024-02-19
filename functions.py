import json
from difflib import get_close_matches
import os
from dotenv import load_dotenv
from typing import Optional
from flask import request

#Environmental variables
load_dotenv()
replies = os.getenv('replies')
if replies is not None:
    replies = int(replies)
similarity = os.getenv('similarity')
if similarity is not None:
    similarity = float(similarity)

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
        
def chat_bot(user_input: str):
    knowledge_db: dict = load_knowledge_db('knowledge_db.json')

    if user_input.lower() == 'bye':
        return "Nice to meet you! :)"

    best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_db["questions"]])

    if best_match:
        answer: str = get_answer_for_question(best_match, knowledge_db)
        return answer
    else:
        new_answer: str = input('Type the answer or "skip" to skip: ')

        if new_answer.lower() != 'skip':
            knowledge_db["questions"].append({"question": user_input, "answer": new_answer})
            save_knowledge_db('knowledge_db.json', knowledge_db)
            return 'Thank you! I learned something new today!'
        else:
            return 'Ok, no problem!'



        