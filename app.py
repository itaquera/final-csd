from flask import Flask, request, jsonify
from app.auth.services import AuthenticationService
from app.user.services import UserService
from app.user.infrastructure.user_repository import UserRepository

app = Flask(__name__)

# Criação do repositório e serviços
user_repository = UserRepository()
user_service = UserService(user_repository)
auth_service = AuthenticationService(user_repository)

# Endpoint para criação de usuário
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    try:
        user_id = user_service.create_user(username, password)
        return jsonify({'user_id': user_id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

# Endpoint para autenticação
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if auth_service.login(username, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)
