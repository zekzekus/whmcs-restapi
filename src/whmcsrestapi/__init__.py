from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<model>/<action>", methods=["GET"])
def client(model, action):
    return "%s - %s" % (model, action)


def main():
    app.run()


if __name__ == "__main__":
    app.run()
