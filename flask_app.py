from flask import Flask, render_template, make_response, request, redirect
from hashlib import sha256
import psycopg2


app = Flask(__name__)

def getConnection(host, port, database, user, password):
    connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password)
    return connection

def getConnection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="user_data",
        user="postgres",
        password="kclds123")
    return connection

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
    connection = getConnection()
    cursor = connection.cursor()
    query = """ SELECT password from user_credentials WHERE email=%s """
    cursor.execute(query, (email,))
    database_password = cursor.fetchone()[0]
    if password_hash == database_password:
        print("True")
    else:
        print("False")
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

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
        connection = getConnection()
        cursor = connection.cursor()
        query = """ INSERT INTO user_credentials (fname, lname, email, password) VALUES (%s,%s,%s,%s)"""
        data = (fname, lname, email, password_hash)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()
    return redirect('/')

if __name__ == '__main__':
   app.run()