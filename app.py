from flask import Flask, render_template, url_for
from flask import request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://franco:Fa101325@localhost/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"


db =  SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}
     

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('get_users'))

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_form')
def user_form():
    return render_template('user_form.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()    
    app.run(host='0.0.0.0', debug=True)