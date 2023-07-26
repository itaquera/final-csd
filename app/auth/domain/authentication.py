class Authentication:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, username, password):
        user = self.user_repository.get_by_username(username)
        if user and user.is_active and self._verify_password(user, password):
            return True
        return False

    def _verify_password(self, user, password):
        return user.password == password
