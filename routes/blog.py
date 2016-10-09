from routes import *
from models.blog import Blog


main = Blueprint('blog', __name__)


@main.route('/')
def index():
    blog_list = Blog.query.order_by(Blog.created_time.desc()).all()
    return render_template('blog/index.html', blog_list=blog_list)


@main.route('/write')
@login_required
def write():
    return render_template('blog/write.html')


@main.route('/edit/<int:id>')
@login_required
def edit(id):
    blog = Blog.query.filter_by(id=id).first()
    if blog is not None:
        return render_template('blog/edit.html', blog=blog)
    else:
        return abort(404)


@main.route('/add', methods=['POST'])
@login_required
def add():
    blog = Blog(request.form)
    if blog.validate_add:
        blog.save()
        flash(u'发表成功')
        return redirect(url_for('blog.blog', id=blog.id))
    else:
        flash(u'请输入标题')
    return redirect(url_for('blog.index'))


@main.route('/update/<int:id>', methods=['POST'])
@login_required
def update(id):
    form = request.form
    b = Blog(form)
    blog = Blog.query.get(id)
    if blog is not None and b.validate_add:
        blog.title = b.title
        blog.body = b.body
        blog.save()
        flash(u'修改成功')
        return redirect(url_for('blog.blog', id=id))
    return redirect(url_for('blog.edit', id=id))


@main.route('/delete/<int:id>')
@login_required
def delete(id):
    blog = Blog.query.get(id)
    if blog is not None:
        blog.delete()
        flash(u'删除文章成功')
        return redirect(url_for('blog.index'))
    return abort(404)


@main.route('/<int:id>')
def blog(id):
    blog = Blog.query.filter_by(id=id).first()
    if blog is not None:
        return render_template('blog/blog.html', blog=blog)
    return redirect(url_for('blog.index'))