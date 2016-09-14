#! -*- coding: utf-8 -*-
from flask import render_template, session, redirect, request, url_for, flash
from . import auth
from .forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User
from ..utils import log
from .. import db

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user =  User(email= form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(u'注册成功')
        return redirect(url_for('main.index'))
    return render_template('auth/auth.html', where="register", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        form.password.errors = [u'用户名或密码错误']
    return render_template('auth/auth.html', where="login", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'你已经注销')
    return redirect(url_for('main.index'))
