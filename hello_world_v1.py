from flask import Flask
from os import environ

app = Flask(__name__)

'''
@app.route("/")
def hi_person():
    return "welcome to the new coding world"
'''

@app.route("/hello/<name>")

def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
if __name__ == '__main__':
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
