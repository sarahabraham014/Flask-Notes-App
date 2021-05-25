from flask import Blueprint, render_template
from website import create_app

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)