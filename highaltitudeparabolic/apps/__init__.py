import logging
import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .. import config
from flask_login import LoginManager
from flask_restful import Api
from apscheduler.schedulers.background import BackgroundScheduler



app = Flask(__name__)
restful_api = Api(app)
app.config.from_object(config)

# 允许跨域请求
cors = CORS(app, resources=r'/*', supports_credentials=True)

# 显示中文
app.config['JSON_AS_ASCII'] = False

login_manager = LoginManager()  # 初始化flask_login
login_manager.session_protection = 'strong'  # 设置登录安全级别
login_manager.login_view = 'login'  # 指定了未登录时跳转的页面
login_manager.init_app(app)

# Logging
log = logging.getLogger()
log.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
app.logger.setLevel(app.config.get('LOG_LEVEL', "INFO"))
app.logger.addHandler(handler)

db = SQLAlchemy(app, session_options=dict(autocommit=False, autoflush=True))


@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
        db.session.remove()
    db.session.remove()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='favicon.icon')


# 创建数据库
from .model.camera import *
from .model.video import *
from .model.event import *
from .router.router import regist_router


def init_database():
    db.init_app(app)
    db.create_all()


def initialize():
    init_database()
    regist_router()
