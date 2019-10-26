from flask import Flask, request
app = Flask(__name__)


@app.route('/payload', methods = ['POST'])
def hello():
    return {"msg" : "this is done"}


if __name__ == '__main__':
    app.run()