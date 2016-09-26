#! -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp


class LoginForm(Form):
    email = StringField(u'邮箱', validators = [Required(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators = [Required()])
    remember_me = BooleanField(u'保持登录')
    submit= SubmitField(u'登录')
