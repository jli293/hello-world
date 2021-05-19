from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    prints "hello world from flaskland"
    """

    return "<p>Hello World from Flaskland!</p>"


if __name__ == '__main__':
    app.run()
