from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/salom')
@app.route('/ok')
@app.route("/hi")
def hi():
    return "<h1>Hi, World!</h1>"


if __name__ == '__main__':
    app.run(debug=True)