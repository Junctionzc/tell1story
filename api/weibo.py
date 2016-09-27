from routes import *
from models.weibo import Weibo
from utils import log

import json


main = Blueprint('api_weibo', __name__)


@main.route('/update', methods=["POST"])
@login_required
def update():
    form = request.form
    weibo_id = form.get('weibo_id')
    log('weibo id', weibo_id)
    weibo_content = form.get('weibo_content')
    log('weibo content', weibo_content)
    r = {
        'data': []
    }

    w = Weibo.query.filter_by(id=int(weibo_id)).first()
    log('w', w)
    if w is not None:
        w.content = weibo_content
        w.save()
        r['success'] = True
        r['data'] = w.json()
    else:
        r['success'] = False
        r['message'] = '参数错误'

    return json.dumps(r, ensure_ascii=False)
