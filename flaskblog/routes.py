from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

import matlab.engine


    
@app.route('/')
def home():
    return render_template('home.html')


@app.route("/account")
def account():
    eng = matlab.engine.start_matlab()
    e = eng.launch(nargout=0)
    input("Press Enter to continue...")
    return e

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.create_all()
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/homepage')
def homepage():
    return render_template('pp.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/plant')
def plant():
    return render_template('plant.html')

@app.route('/pred')
def pred():
    return render_template('pred.html')



@app.route('/haemoglobin')
def haemoglobin():
    return render_template('haemoglobin.html')

@app.route('/leghemoglobin')
def leghemoglobin():
    return render_template('leghemoglobin.html')

@app.route('/symbiotic')
def symbiotic():
    return render_template('symbiotic.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')




