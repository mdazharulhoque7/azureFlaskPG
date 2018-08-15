from flask import Flask
from sqlalchemy import MetaData, create_engine
from extensions import (db,

                            )

def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    # app_instance = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder="static")
    #
    # app_instance.config.from_object('config.settings')
    # app_instance.config.from_pyfile('settings.py', silent=True)
    #
    # if settings_override:
    #     app_instance.config.update(settings_override)

    app_instance = Flask(__name__, static_url_path='', static_folder="static")
    app_instance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app_instance.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
        # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
        'manager@contextiapgs', 'supersecretpass', 'contextiapgs.postgres.database.azure.com', 'eventregistration'
    ) + '?sslmode=require'


    app_instance = extensions(app_instance)
    app_instance = register_blueprint(app_instance)
    # authentication(app_instance)
    # CORS(app_instance)

    return app_instance



def extensions(app_instance):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    # debug_toolbar.init_app(app)
    # mail.init_app(app_instance)
    # csrf.init_app(app_instance)
    db.init_app(app_instance)
    # login_manager.init_app(app_instance)

    # app.config.update({
    #     'RESTFUL_JSON':{
    #         'cls':CustomJSONEncoder
    #     }
    # })
    # app.json_encoder = CustomJSONEncoder
    # flask_restful.representations.json.settings["cls"] = CustomJSONEncoder

    # metaData = MetaData()
    # engine = create_engine(app_instance.config['SQLALCHEMY_DATABASE_URI'], pool_recycle=3600, pool_size=20, max_overflow=-1)
    # metaData.bind = engine
    # engine.echo = False
    #
    #
    # session_factory = sessionmaker(bind=engine, autoflush=False)
    # session = flask_scoped_session(session_factory, app_instance)


    return app_instance

def register_blueprint(app_instance):
    from blueprints import default_blueprint
    # from app.blueprints.api.presence_data import presence_data_blueprint
    # from app.blueprints.api.presence_summary import presence_summary_blueprint

    # app_instance.register_blueprint(presence_data_blueprint, url_prefix='/presence_data')
    # app_instance.register_blueprint(presence_summary_blueprint, url_prefix='/presence_summary')
    app_instance.register_blueprint(default_blueprint)

    return app_instance




# def authentication(app_instance):
#     """
#     Initialize the Flask-Login extension (mutates the app passed in).
#
#     :param app: Flask application instance
#     :param user_model: Model that contains the authentication information
#     :type user_model: SQLAlchemy model
#     :return: None
#     """
#     login_manager.login_view = 'user.login'
#
#     @login_manager.user_loader
#     def load_user(user_id):
#         from blueprints.user.models import UserModel
#         return UserModel.query.get(user_id)
#
#     return None