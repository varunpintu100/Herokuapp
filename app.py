from flask import Flask,render_template,request,flash
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = "Varun"
api = Api(app)
jwt = JWT(app,authenticate,identity) # /auth

@app.route("/")
def index():
    flash("PLease enter your login details!!!")
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = str(request.form['username_input'])
    password = str(request.form['password_input'])
    if authenticate(username,password):
        return render_template("login.html"),200
    else:
        return render_template("Error.html"),404
api.add_resource(UserRegister,'/register')