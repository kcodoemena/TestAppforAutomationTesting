# Import necessary modules from Flask
from flask import Flask, request, jsonify
import re  # Import regex module for pattern matching

# Initialize the Flask application
app = Flask(__name__)


# Function to validate the registration form data
def validate_registration(data):
    errors = []  # List to collect validation error messages

    # Check if the first name is provided and not empty
    if not data.get('first_name'):
        errors.append("First name is required.")

    # Check if the last name is provided and not empty
    if not data.get('last_name'):
        errors.append("Last name is required.")

    # Check if the email is provided and has a valid format
    email = data.get('email')
    if not email:
        errors.append("Email is required.")
    # Regex pattern to validate email format
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        errors.append("Invalid email format.")

    # Check if the password meets length and character requirements
    password = data.get('password')
    if not password:
        errors.append("Password is required.")
    elif len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    elif not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
    elif not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")
    elif not re.search(r"[0-9]", password):
        errors.append("Password must contain at least one number.")
    elif not re.search(r"[!@#$%^&*()_+]", password):
        errors.append("Password must contain at least one special character.")

    return errors  # Return the list of errors if any


# Define the registration endpoint to handle POST requests
@app.route('/register', methods=['POST'])
def register():
    data = request.json  # Get JSON data from the request
    errors = validate_registration(data)  # Validate the input data

    # If there are validation errors, return them with a 400 status code
    if errors:
        return jsonify({"success": False, "errors": errors}), 400
    # If validation passes, return a success message with a 200 status code
    return jsonify({"success": True, "message": "Registration successful."}), 200


# Run the Flask application when the script is executed
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for easier troubleshooting
