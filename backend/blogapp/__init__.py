# make this a package and restructure the project
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)  # allow db to handle sessions
login_manager.login_view = "login"
login_manager.login_message_category = "danger"

# posts = [{"author": "kamaa", "year": "2002"}, {"author": "jane", "year": "2012"}]
# posts = [{}]
app.config["SECRET_KEY"] = "fac58fa2c3413763fbb7"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

CORS(app)
db = SQLAlchemy(app)

# avoid circular imports
from blogapp import routes
