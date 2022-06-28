import os
from flask_migrate import Migrate
from flask_cli import FlaskCLI
from main.models import db
from main import create_app

application = create_app("dev")

if __name__ == "__main__":
    with application.app_context():
        db.create_all()
        application.run()


