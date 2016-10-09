from . import db
from . import ModelMixin
from . import timestamp


class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    created_time = db.Column(db.Integer)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)

    def __init__(self, form):
        self.created_time = timestamp()
        self.title = form.get('title', '')
        self.body = form.get('content', '')
        if len(self.title) > 0:
            self.validate_add = True
        else:
            self.validate_add = False

    def __repr__(self):
        return '<Blog %r>' % self.title
