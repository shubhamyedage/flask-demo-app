from flask import jsonify, Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({"msg": "helloworld!"})