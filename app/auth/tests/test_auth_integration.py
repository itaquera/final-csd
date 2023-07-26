import unittest
from app.auth.services import AuthenticationService
from app.user.services import UserService
from app.user.infrastructure.user_repository import UserRepository

class TestAuthenticationIntegration(unittest.TestCase):
    def test_successful_login(self):
        user_repository = UserRepository()
        user_service = UserService(user_repository)
        user_id = user_service.create_user("username", "password")
        auth_service = AuthenticationService(user_repository)
        result = auth_service.login("username", "password")
        self.assertTrue(result)

    def test_failed_login(self):
        user_repository = UserRepository()
        auth_service = AuthenticationService(user_repository)
        result = auth_service.login("username", "wrong_password")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
