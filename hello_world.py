from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    prints "hello world from flaskland"
    """

    return "<p>Hello World from Flaskland!</p>"

 print ("My name is Efua. Welcome to PennChats")
 print("Hello it's SPARC not SPRAC")
 print("Audra's comment")
 print("Sarah's comments")

if __name__ == '__main__':
    app.run()
