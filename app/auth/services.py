from app.auth.domain.authentication import Authentication

class AuthenticationService:
    def __init__(self, user_repository):
        self.authentication = Authentication(user_repository)

    def login(self, username, password):
        return self.authentication.login(username, password)
