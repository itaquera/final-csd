from app.user.domain.user import User

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, username, password):
        if self.user_repository.get_by_username(username):
            raise ValueError("Usuário já existe.")

        user_id = self.user_repository.get_next_id()
        user = User(user_id, username, password)
        self.user_repository.save(user)
        return user_id

    def get_user(self, username):
        return self.user_repository.get_by_username(username)

    def deactivate_user(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado.")

        user.deactivate()
        self.user_repository.save(user)
