"""
from flask import Flask



app = Flask(__name__)

# Flask is designed in terms of Routes. Where routes is part of the URL that you type in to determine the request.
@app.route("/")
def index():
    return "Hello, world!"
# Might need to specify in terminal: 
# export FLASK_APP=app.py


Using waitress as a server host (Waitress WSGI Server): 
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port = 8080)
To run: 
python3 <pythonfile>


{{}} Can be used to subsitute a variable to it. 
test = "something"
<h1> {{test}} </h1>

To control what content to display: 
{% if new_year %}
    <h1>It is New Years! </h1>
{% else %}
    <h1>No, it's not new years</h1>
{% endif %}


Loops in flask:
<ul>
{% for name in names %}
<li>{{name}}</li>
{% endfor %}


To create session: 
from flask import session
from flask_session improt Session

app.config["SESSION_TYPE"] = "filesystem"

notes=[]

@app.route('/')
def index():
    if session.get("notes") is None:
        session["notes"] = []
    session"notes" = []
    if request.method = 'post':
        note = request.form.get("note")
        session["note"].append(note)
    return render_template("index.html", notes=session["notes"])


"""

