# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import status
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('PW.html')

@app.route('/password', methods = ['GET', 'POST'])
def password():
    if request.method == "GET":
        return render_template('PW.html')
    else:
        print(request.form)
        choice = request.form['choice']
        password_length = request.form['password_length']
        new_password = status(password_length , choice)
        username = request.form['username']
        return render_template('manage.html', password_length =  password_length, choice =  choice, new_password =   new_password, username = username)
# @app.route('/password/encrypt', methods = ['GET', 'POST'])
# def encrypt():
#     if request.method == "GET":
#         return render_template('PW.html')
#     else:
#         print(request.form)
#         password_length = request.form['password_length']
#         new_password = password
#         username = request.form['username']
#         return render_template('encrypt.html', password_length =  password_length, new_password =   new_password, username = username)




        
                




