class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def __repr__(self):
        return f"User(user_id={self.user_id}, username='{self.username}', is_active={self.is_active})"
