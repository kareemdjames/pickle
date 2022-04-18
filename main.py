from flask import Flask, render_template
from data import start

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', charlist=start())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
