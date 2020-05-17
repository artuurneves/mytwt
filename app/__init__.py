from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server



app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)

manager = Manager(app=app)
manager.add_command('runserver', Server(host='0.0.0.0', port='5000'))
manager.add_command('db', MigrateCommand)

from app.controllers import default