from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:copland1@35.189.108.24/flask_db"

db = SQLAlchemy(app)

from application import routes