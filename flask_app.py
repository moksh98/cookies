from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route("/")
def home():
    response = make_response(render_template('index.html'))
    arr = [1, 2, 3]
    response.headers["Set-Cookie"] = "myfirstcookie="+str(arr)
    return response

if __name__ == '__main__':
   app.run()