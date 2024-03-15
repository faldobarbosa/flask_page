from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv




load_dotenv()

# db = SQLAlchemy()

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://franco:Fa101325@localhost/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"

db =  SQLAlchemy(app)