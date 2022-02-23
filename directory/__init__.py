from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from directory.config import Development
from directory.utils.responses import DefaultResponse

# Init flask app
app = Flask(__name__)
app.config.from_object(Development)

# Connect flask to sqlalchemy
db = SQLAlchemy(app)

# Connect flask to flask-migration
migrate = Migrate(app, db)

# JWT Token
jwt_manager = JWTManager(app)


@app.route('/')
def index():
    return {'msg': "App work"}


from directory.apps.app_users import users
app.register_blueprint(users, url_prefix='/api/v1/users/')
