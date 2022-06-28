from flask import Flask, make_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    response = make_response("Here, take some cookie!")
    arr = [1, 2, 3]
    response.headers["Set-Cookie"] = "myfirstcookie="+str(arr)
    return response

if __name__ == '__main__':
   app.run()