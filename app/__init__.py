from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app.model import user, dosen, mahasiswa, gambar






