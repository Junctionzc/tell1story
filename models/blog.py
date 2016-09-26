from . import db
from . import ModelMixin


class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    created_time = db.Column(db.Integer)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)

    def __init__(self, form):
        pass

    def __repr__(self):
        return '<Blog %r>' % self.title
