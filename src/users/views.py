from flask import Blueprint, render_template, request, session, redirect, url_for

from src.users.forms import SignupForm, LoginForm
from src.users.models import User
from src.ext import db


bp_users = Blueprint('users', __name__)


@bp_users.route("/signup", methods=["GET", "POST"])
def signup():
    if 'email' in session:
        return redirect(url_for('home'))

    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            return redirect(url_for('home'))

    elif request.method == "GET":
        return render_template('signup.html', form=form)


@bp_users.route("/login", methods=["GET", "POST"])
def login():
    if 'email' in session:
        return redirect(url_for('home'))

    form = LoginForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    elif request.method == 'GET':
        return render_template('login.html', form=form)


@bp_users.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


@bp_users.route("/home", methods=["GET", "POST"])
def home():
    if 'email' not in session:
        return redirect(url_for('login'))

    form = AddressForm()

    places = []
    my_coordinates = (37.4221, -122.0844)

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('home.html', form=form)
        else:
            # get the address
            address = form.address.data

            # query for places around it
            p = Place()
            my_coordinates = p.address_to_latlng(address)
            places = p.query(address)

            # return those results
            return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)

    elif request.method == 'GET':
        return render_template("home.html", form=form, my_coordinates=my_coordinates, places=places)
