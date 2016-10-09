from api import *
from utils import log

import json, time, hashlib, os

from werkzeug import secure_filename


main = Blueprint('api_blog', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@main.route('/upload/picture', methods=["POST"])
@login_required
def upload_picture():
    log('fuck')
    picture = request.files['file_upload_picture']
    log('picture', picture)
    r = {
        'data': []
    }
    if picture and allowed_file(picture.filename):
        hash = hashlib.md5(picture.filename.encode('utf-8')).hexdigest()
        upload_time = int(time.time())
        extension = secure_filename(picture.filename).split('.')[-1]
        filename = '{}_{}.{}'.format(hash, upload_time, extension)
        picture.save(os.path.join(current_app.config['BLOG_FOLDER'], filename))
        picture_url = url_for('api_blog.picture', picture_name=filename)
        r['success'] = True
        r['data'] = dict(
            picture_url = picture_url,
        )
    else:
        r['success'] = False
        r['message'] = '上传失败'
    return json.dumps(r, ensure_ascii=False)


@main.route('/picture/<picture_name>')
def picture(picture_name):
    return send_from_directory(current_app.config['BLOG_FOLDER'], picture_name)