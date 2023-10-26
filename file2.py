from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def vipul():
    name = "Vipul"
    return render_template('about.html', name = name)

@app.route("/boostrape")
def boostrape():
    return render_template('boostrape.html')

app.run()