from routes import *


main = Blueprint('blog', __name__)


@main.route('/')
def index():
    return render_template('blog/blog_index.html')
