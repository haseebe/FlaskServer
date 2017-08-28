from flask import Flask

app = Flask(__name__)


@app.route('/home')
def home():
    return "hello world"

@app.route('/successful')
def success():
    return "<h1>CONGRATULATIONS BUDDY, YOU'RE IN!</h1>"

if __name__ == '__main__':
    app.run()
