from flask import Flask, render_template, url_for
from flask import request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from database import db



load_dotenv()


app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://franco:Fa101325@localhost/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"


db.init_app(app)

from views import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()    
    app.run(host='0.0.0.0', debug=True)