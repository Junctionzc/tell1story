from routes import *


main = Blueprint('tool', __name__)


@main.route('/')
def index():
    return render_template('tool/tool_index.html')
