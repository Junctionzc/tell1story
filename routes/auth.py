from routes import *
from forms.auth import LoginForm
from models.user import User


main = Blueprint('auth', __name__)


@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('weibo.index'))
    return redirect(url_for('.login'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('weibo.index'))
        flash(u'用户名或密码错误')
    return render_template('auth/login1.html', form = form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'你已经注销')
    return redirect(url_for('weibo.index'))


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
