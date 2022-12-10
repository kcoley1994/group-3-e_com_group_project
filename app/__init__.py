from flask import Flask
from config import Config
from flask_migrate import Migrate

from .models import db, User
from .auth.routes import auth

app = Flask(__name__)

app.config.from_object(Config)

# register blueprints
app.register_blueprint(auth)

# initialize database to work with app
db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models
