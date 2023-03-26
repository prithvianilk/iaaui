from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=["GET", "POST"])
def get():
    return "<h1>This is my flask application</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
