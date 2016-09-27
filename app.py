#! -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

from models import db, login_manager
from models.user import User
from models.blog import Blog
from models.weibo import Weibo

from routes.auth import main as routes_auth
from routes.blog import main as routes_blog
from routes.weibo import main as routes_weibo
from routes.tool import main as routes_tool
from api.weibo import main as api_weibo


bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(routes_auth, url_prefix = '/auth')
    app.register_blueprint(routes_blog, url_prefix = '/blog')
    app.register_blueprint(routes_weibo)
    app.register_blueprint(routes_tool, url_prefix = '/tool')
    app.register_blueprint(api_weibo, url_prefix = '/api/weibo')

    return app
