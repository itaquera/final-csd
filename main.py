import unittest
from app.auth.tests.test_auth_integration import TestAuthenticationIntegration
from app.user.tests.test_user_integration import TestUserIntegration

if __name__ == "__main__":
    auth_tests = unittest.TestLoader().loadTestsFromTestCase(TestAuthenticationIntegration)
    user_tests = unittest.TestLoader().loadTestsFromTestCase(TestUserIntegration)
    all_tests = unittest.TestSuite([user_tests, auth_tests])

    unittest.TextTestRunner(verbosity=2).run(all_tests)
