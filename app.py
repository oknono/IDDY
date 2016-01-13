from flask import Flask, render_template, jsonify
from dead_or_alive import Wiki_Person
import requests
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dick = Wiki_Person("Dick Cheney")
    dick_dead = dick.is_dead()

    dead_text = ["Dick Cheney is Dead!", "Dick is still dead", "Dick Cheney is no longer alive",
                 "Dick Cheney has seized to be", "Yes, Dick Cheney is dead",
                 "Yes, Dick Cheney is Dead!", "Yes, Dick is still dead", "No, Dick Cheney is no longer alive",
                 "Yes, Dick Cheney has seized to be", "Yes, Dick Cheney is dead"]
    alive_text = ["Dick Cheney is not dead yet...", "Dick Cheney is still alive",
                  "Dick Cheney is still breathing", "Dick Cheney is not dead",
                  "No, Dick Cheney is not dead yet...",
                  "Yes, yes, Dick Cheney is still breathing", "No, Dick Cheney is not dead"]
    if dick_dead:
        name = "dead"
        result= dead_text[random.randrange(len(dead_text))]
    else:
        name = "alive"
        result = alive_text[random.randrange(len(alive_text))]
    return render_template('index.html', name=name, result=result )

@app.route('/api', methods=['GET'])
def get_dick():
    dick = Wiki_Person("Dick Cheney")
    dick_dead = dick.is_dead()
    return jsonify({'dick_is_dead': dick_dead})

if __name__ == '__main__':
    app.run()
