from flask import Flask, request, jsonify

app = Flask(__name__)

dishes = []


@app.route('/dish', methods=["GET", "POST"])
def get():
    if request.method == "GET":
        return jsonify(dishes)
    elif request.method == "POST":
        dishes.append(request.get_json())
        return "OK", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
