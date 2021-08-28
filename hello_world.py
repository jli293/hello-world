from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    prints "hello world from flaskland"
    """

    return "<p>Hello World from Jimmy!</p>"

if __name__ == '__main__':
    app.run()
