from flask import Flask, render_template, request, jsonify
from functions import chat_bot

app = Flask(__name__)

@app.route('/')
def chatbot_interface():
    return render_template('chatbot_interface.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = chat_bot(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    print('------------------------------------------ \n')
    print('Hello! I\'m Josete and I\'m here to assist you :) \n')
    print('------------------------------------------ \n')
    app.run(debug=True)
