from flask import Flask, render_template

app = Flask(__name__, template_folder='path/to/custom/templates')


@app.route('/')
def chatbot_interface():
    return render_template('chatbot_interface.html')

if __name__ == '__main__':
    app.run(debug=True)


