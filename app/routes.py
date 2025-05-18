from flask import Blueprint, jsonify
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({'message': 'Welcome!'})

@main.route('/users')
def users():
    return jsonify([{'id': user.id, 'username': user.username} for user in User.query.all()])