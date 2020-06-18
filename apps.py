from flask import Flask,render_template,request

import mysql.connector

app=Flask(__name__)

imDB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
)
db=imDB.cursor()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username=request.form.get("username")
    password=request.form.get("password")
    error="If u don't have account sign up"
    log="login"
    sql="SELECT * FROM login WHERE username=%s AND password =%s"
    value=(username,password)
    db.execute(sql,value)
    user =db.fetchone() 
    if user is None:
        return render_template("error.html", error=error)
    
    else:
        return render_template("success.html", log=log)

@app.route("/account")
def account():
    return render_template("signup.html")

@app.route("/signup",methods=["POST"])
def signup():
    name=request.form.get("name")
    username=request.form.get("username")
    email=request.form.get("email")
    phone=request.form.get("phone_no")
    password_1=request.form.get("password_0")
    password_2=request.form.get("password_1")
    log="Signup"
    sql="SELECT * FROM login WHERE username=%s"
    value=(username,)
    db.execute(sql,value)
    user=db.fetchone()

    if user is None:
        if password_1==password_2:
            sql="INSERT INTO login(name,username,email,phone_no,password) VALUES(%s,%s,%s,%s,%s)"
            value=(name,username,email,phone,password_2)
            db.execute(sql,value)
            imDB.commit()
            return render_template("success.html",log=log)
        else:
            ret="Two pass word are not equal"
            return render_template("signup.html",ret=ret)
    else:
        ret="This user name is already exist"
        return render_template("signup.html",ret=ret)



    