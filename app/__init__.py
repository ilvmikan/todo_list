from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import create
from app.routes import delete
from app.routes import edit
from app.routes import index





