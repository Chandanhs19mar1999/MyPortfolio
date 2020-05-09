from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("page1.html")

@app.route("/resume")
def resume():
    return render_template("page2.html")

@app.route("/contact")
def contact():
    return render_template("page3.html")


if __name__ == '__main__' :
    app.run(port=8000,debug=True)