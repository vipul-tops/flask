from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/fashion")
def fashion():
    return  render_template('fashion.html')

@app.route("/jewellery")
def jewellery():
    return  render_template('jewellery.html')

@app.route("/electronic")
def electronic():
    return  render_template('electronic.html')


app.run(debug=True)