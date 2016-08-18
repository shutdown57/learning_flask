from flask import Flask, render_template

from src.users.views import bp_users
from src.ext import db


app = Flask(__name__)

app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

app.register_blueprint(bp_users, url_prefix='/users')

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
