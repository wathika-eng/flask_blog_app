# make this a package and restructure the project
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
# posts = [{"author": "kamaa", "year": "2002"}, {"author": "jane", "year": "2012"}]
# posts = [{}]
app.config["SECRET_KEY"] = "fac58fa2c3413763fbb7"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"


db = SQLAlchemy(app)

# avoid circular imports
from blogapp import routes
