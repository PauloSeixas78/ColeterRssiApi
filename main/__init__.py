
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from main.models import db
from main.routes import index_main
from main.routes.elemento_bp import elemento_bp
from main.routes.coleta_bp import coleta_bp
from .config import config_por_nome
from sqlalchemy_utils import database_exists, create_database

bcrypt = Bcrypt() 

def create_app(config_env):
    print("criando app")
    app = Flask(__name__)
    app.config.from_object(config_por_nome[config_env])
    db.init_app(app)
    #migrate = Migrate(app,db)
    app.register_blueprint(index_main)
    app.register_blueprint(elemento_bp, url_prefix = "/elemento")
    app.register_blueprint(coleta_bp, url_prefix = "/coleta")
    bcrypt.init_app(app)
    return app

