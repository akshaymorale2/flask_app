import logging
import os
from flask_login import LoginManager
from flask import Flask
from werkzeug.utils import import_string
from .userapp.models import Users, Shouts
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from . import config, db, create_database

from flask_cors import CORS, cross_origin

logger = logging.getLogger(__name__)


def create_app(environment):

    config_map = {
        'development': config.Development(),
        'testing': config.Testing(),
        'production': config.Production(),
    }

    config_obj = config_map[environment.lower()]

    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.url_map.strict_slashes = False
    app.add_url_rule('/', 'home', home)
    db.init_app(app)
    #io.init_app(app)

    register_blueprints(app)

    create_database(app)


    login_manager = LoginManager()

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.filter_by(id=user_id).first()

    admin = Admin(app)
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Shouts, db.session))

    return app


def home():
    return dict(name='Social Flask REST API')


def register_blueprints(app):
    root_folder = 'social_app'
    print(os.getcwd())

    for dir_name in os.listdir(root_folder):
        module_name = root_folder + '.' + dir_name + '.views'
        module_path = os.path.join(root_folder, dir_name, 'views.py')

        if os.path.exists(module_path):
            module = import_string(module_name)
            obj = getattr(module, 'app', None)
            if obj:
                app.register_blueprint(obj)