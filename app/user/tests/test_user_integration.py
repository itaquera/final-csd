import unittest
from app.user.services import UserService
from app.user.infrastructure.user_repository import UserRepository

class TestUserIntegration(unittest.TestCase):
    def test_create_user(self):
        user_repository = UserRepository()
        user_service = UserService(user_repository)
        user_id = user_service.create_user("username", "password")
        self.assertIsNotNone(user_id)

    def test_get_user(self):
        user_repository = UserRepository()
        user_service = UserService(user_repository)
        user_id = user_service.create_user("username", "password")
        user = user_service.get_user("username")
        self.assertIsNotNone(user)

if __name__ == '__main__':
    unittest.main()
