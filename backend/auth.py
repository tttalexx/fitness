from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email уже зарегистрирован')
            return redirect(url_for('auth.register'))

        new_user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash('Регистрация прошла успешно')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            flash('Успешный вход')
            return redirect(url_for('main.index'))
        else:
            flash('Неверный email или пароль')

    return render_template('login.html')
