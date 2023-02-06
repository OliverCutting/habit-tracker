from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from habittracker import config  # type: ignore[attr-defined]

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
app.app_context().push()

from habittracker import routes  # noqa: F401,E402
