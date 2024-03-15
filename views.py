from flask import Flask, jsonify, request, redirect, url_for, render_template
from .database import db
from .models import User
from run import app

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