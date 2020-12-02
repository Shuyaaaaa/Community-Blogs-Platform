import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ECE1779'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:19971014Zbwl@localhost:3306/ece1779ass3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = 1
app.config['MAIL_USERNAME'] = 'jianijiahappy@gmail.com'
app.config['MAIL_PASSWORD'] = 'Jjn123456'
app.config['ADMINS'] = ['jianijiahappy@gmail.com']
mail = Mail(app)

from flaskblog import routes
