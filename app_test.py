# Import the unittest module for testing and the Flask app from the app.py file
import unittest
from app import app

# Define a test case class that inherits from unittest.TestCase
class TestRegistration(unittest.TestCase):

    # Set up the test client before each test runs
    def setUp(self):
        # Create a test client for the Flask application
        self.app = app.test_client()
        # Set the app to testing mode, which provides better error handling
        self.app.testing = True

    # Test case for successful registration
    def test_registration_success(self):
        # Send a POST request with valid registration data
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'Password123!'
        })
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the success message is in the response
        self.assertIn('Registration successful', response.json['message'])

    # Test case for empty first name
    def test_empty_first_name(self):
        # Send a POST request with an empty first name
        response = self.app.post('/register', json={
            'first_name': '',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'Password123!'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('First name is required.', response.json['errors'])

    # Test case for empty last name
    def test_empty_last_name(self):
        # Send a POST request with an empty last name
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': '',
            'email': 'john.doe@example.com',
            'password': 'Password123!'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('Last name is required.', response.json['errors'])

    # Test case for empty email field
    def test_empty_email(self):
        # Send a POST request with an empty email
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': '',
            'password': 'Password123!'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('Email is required.', response.json['errors'])

    # Test case for invalid email format
    def test_invalid_email_format(self):
        # Send a POST request with an invalid email format
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe',
            'password': 'Password123!'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('Invalid email format.', response.json['errors'])

    # Test case for short password
    def test_short_password(self):
        # Send a POST request with a short password
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'Short1!'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('Password must be at least 8 characters long.', response.json['errors'])

    # Test case for password missing an uppercase letter
    def test_password_missing_uppercase(self):
        # Send a POST request with a password missing an uppercase letter
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'password123!'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('Password must contain at least one uppercase letter.', response.json['errors'])

    # Test case for password missing a lowercase letter
    def test_password_missing_lowercase(self):
        # Send a POST request with a password missing a lowercase letter
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'PASSWORD123!'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('Password must contain at least one lowercase letter.', response.json['errors'])

    # Test case for password missing a number
    def test_password_missing_number(self):
        # Send a POST request with a password missing a number
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'Password!'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('Password must contain at least one number.', response.json['errors'])

    # Test case for password missing a special character
    def test_password_missing_special_character(self):
        # Send a POST request with a password missing a special character
        response = self.app.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'Password123'
        })
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        # Check that the appropriate error message is in the response
        self.assertIn('Password must contain at least one special character.', response.json['errors'])

# Run the test suite when the script is executed
if __name__ == '__main__':
    unittest.main()
