from flask import Flask, render_template, request



app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    headline = "Dennis Li - QA Engineer"
    return render_template('index.html', headline = headline,)

@app.route("/about")
def resume():
    return ("<h1>About Me Page</h1>")

@app.route("/skills")
def skills():
    skills = ['Python','Selenium', 'Test Case Development','Scrum', 'Agile','Testing Methodologies','Load Testing']
    return render_template('skills.html', skills= skills)

@app.route('/experience')
def experience():
    return render_template('experience.html', title = "Experience")

@app.route("/contact")
def contact():
    return render_template('contact.html',title = "Contact")

@app.route("/<string:name>")
def hello(name):
    # name = name.capitalize()
    # return (f"Hello, {name}")
    return "ERROR: PAGE NOT FOUND"

if __name__ == "__main__":
    FLASK_DEBUG=1
    # from waitress import serve
    # serve(app, host="0.0.0.0", port = 8080)