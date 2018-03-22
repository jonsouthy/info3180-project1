from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "Hxx88F4snT"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresl://dnmvbfumjeivou:6f0efcfb5282c8c6124e83a07e44f144ff129748a385dba08401abe7bb8d4496@ec2-107-20-233-240.compute-1.amazonaws.com:5432/d23p98m4k90en0"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
