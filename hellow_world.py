from flask import Flask
from os import environ

app = Flask(__name__)

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
'''

# based on the URL formatting user's first and last name
@app.route("/jedi/<lastname>/<firstname>")

def hello_person(lastname,firstname):
    list1 = lastname.title().lower()
    list2 = firstname.title().lower()
    
    return "Jedi name is {}".format(list2[:3]+list1[:2])

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
