from routes import *
from models.weibo import Weibo
from utils import log


main = Blueprint('weibo', __name__)


@main.route('/')
def index():
    weibo_list = Weibo.query.order_by(Weibo.created_time.desc()).all()
    return render_template('weibo/weibo_index.html', weibo_list=weibo_list)


@main.route('/add', methods=["POST"])
def add():
    form = request.form
    w = Weibo(form)
    if w.valid():
        w.save()
    return redirect(url_for('.index'))

@main.route('/delete/<int:id>')
def delete(id):
    w = Weibo.query.filter_by(id=id).first()
    if w is not None:
        w.delete()
    return redirect(url_for('.index'))