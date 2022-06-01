from email.mime import application
import os
import unittest

from flask_migrate import Migrate
from flask_cli import FlaskCLI

from main import create_app
from main.models import db

application = create_app('dev')

application.app_context().push()

FlaskCLI(application)

migrate = Migrate(application, db)



if __name__ == "__main__":
    application.run()


