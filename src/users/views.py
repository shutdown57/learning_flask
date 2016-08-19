from flask import Blueprint, render_template, request, session, redirect, url_for

from src.users.forms import SignupForm, LoginForm
from src.users.models import User
from src.ext import db


bp_users = Blueprint('users', __name__)


@bp_users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':

        if form.validate() == False:
            return render_template('signup.html', form=form)

        else:
            new_user = User(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return 'Success!'

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@bp_users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)

    elif request.method == 'POST':

        if form.validate() == False:
            return render_template('login.html', form=form)

        else:

            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()

            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))

            else:
                return redirect(url_for('login'))


@bp_users.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


@bp_users.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')