from src.ext import db
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):

    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(54))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password, salt_length=16)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
