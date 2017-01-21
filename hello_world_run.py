from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route("/")
def template_test_noargument():
    return render_template('hello_world_v1.html')

@app.route ("/jedi/<lastName>/<firstName>")
def template_test(lastName,firstName):
    return render_template('hello_world.html',lastName=lastName.title().lower(),firstName=firstName.title().lower())
    
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)
