# user.py
from flask import Blueprint, request, jsonify
from app.services.user_services import UserService

bp = Blueprint('user', __name__)

@bp.route('/users/test', methods=['GET'])
def test():
    return jsonify({'message': 'Users test route'}), 200

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService().create_user(data['name'], data['email'], data['password'])

    return jsonify(user), 201
