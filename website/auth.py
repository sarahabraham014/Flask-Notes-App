from flask import Blueprint,render_template

auth = Blueprint('auth', __name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html",boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/signup',methods=['GET','POST'])
def sign_up():
    return "<p>Sign Up</p>"
