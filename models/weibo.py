from . import db
from . import ModelMixin
from utils import log

import time


class Weibo(db.Model, ModelMixin):
    __tablename__ = 'weibos'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_time = db.Column(db.Integer)

    def __init__(self, form):
        log('form', form)
        self.content = form.get('weibo', '')
        self.created_time = int(time.time())

    def __repr__(self):
        return '<Blog %r>' % self.title

    def valid(self):
        if len(self.content) > 0 and len(self.content) < 128:
            return True
        else:
            return False

    def get_localtime(self):
        value = time.localtime(self.created_time)
        y = time.strftime('%Y', value)
        m = time.strftime('%m', value)
        d = time.strftime('%d', value)
        t = time.strftime('%H:%M:%S', value)
        dt = '{}年{}月{}日 {}'.format(y, m, d, t)
        return dt