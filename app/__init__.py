from flask import Flask
from flask_bootstrap import Bootstrap

from app.quartzJob.schedulerJob import Quartz
from main import configSingle
from models import initDb, User
import ConfigParser
import os

bootstrap = Bootstrap()
db = initDb()
quartz = Quartz()
configInstance = configSingle.ConfigObj()
def create_app():
    app = Flask(__name__)
    app.secret_key = 'unable to guessing pwd!@#$%'

    configInstance.config_obj.set("project_conf", "base_dir", os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    configInstance.flushConfig()

    bootstrap.init_app(app)

    sched = quartz.addJobDynamic()
    sched.start()
    # register routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .common import common as common_blueprint
    app.register_blueprint(common_blueprint, url_prefix='/common')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api')

    from .test import test as test_blueprint
    app.register_blueprint(test_blueprint, url_prefix='/test')

    return app
