from flask import Flask, render_template, make_response, request, redirect
from hashlib import sha256

app = Flask(__name__)


def getHash(string):
    hash = sha256()
    hash.update(bytes(string, "utf-8"))
    return hash.hexdigest()

@app.route("/")
def home():
    response = make_response(render_template('index.html'))
    arr = [1, 2, 3]
    response.headers["Set-Cookie"] = "myfirstcookie="+str(arr)
    return response

@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/signup/")
def signup():
    return render_template('signup.html')

@app.route("/get_login", methods=["POST"])
def get_login():
    email = request.form['email']
    password = request.form['psw']
    password_hash = getHash(password)
    # print(f"Email: {email}, Password: {password_hash}")
    return redirect('index.html')

@app.route("/get_signup", methods=["POST"])
def get_signup():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['psw']
    password_repeat = request.form['psw-repeat']
    password_hash = getHash(password)
    password_repeat_hash = getHash(password_repeat)
    if password_hash == password_repeat_hash:
        pass
        # print(f"First Name: {fname}, Last Name: {lname}, Email: {email}, Password: {password_hash}, Repeat Password: {password_repeat_hash}")
    return redirect('/')

if __name__ == '__main__':
   app.run()