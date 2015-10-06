from flask import Flask, render_template
import requests
from wiki_JSON import categories, is_dead

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Dick%20Cheney&continue=&prop=categories&format=json'
    r = requests.get(url)
    d = categories(r)
    if is_dead(d):
        name = "dead"
        result = "Dick Cheney is Dead!"
    else:
        name = "alive"
        result = "Dick Cheney is not dead yet..."
    return render_template('index.html', name=name, result=result, text=name)

if __name__ == '__main__':
    app.run()
