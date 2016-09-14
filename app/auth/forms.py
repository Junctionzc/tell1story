#! -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User
from ..utils import log

class RegistrationForm(Form):
    email = StringField(u'电子邮箱', validators=[Required(), Length(1, 64), Email(u'邮箱格式不正确')])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z0-9_.]*$', 0, u'用户名必须为字母，数字，点或者下划线')])
    password = PasswordField(u'密码', validators=[Required()])

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            log('error')
            raise ValidationError(u'邮箱已经被注册')

    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError(u'用户名已经被使用')

class LoginForm(Form):
    email = StringField(u'电子邮箱', validators=[Required(), Length(1, 64), Email(u'邮箱格式不正确')])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'记住我')
