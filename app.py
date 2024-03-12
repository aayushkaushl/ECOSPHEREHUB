from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for user information (replace with a database in a production environment)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        # Get user details from the registration form
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username is already taken
        if username in users:
            return jsonify({'status': 'error', 'message': 'Username is already taken'})

        # Store user information in the users dictionary
        users[username] = {
            'name': name,
            'email': email,
            'phone': phone,
            'age': age,
            'password': password
        }

        return jsonify({'status': 'success', 'message': 'Registration successful'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/login', methods=['POST'])
def login():
    try:
        # Get login credentials from the login form
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username exists and the password is correct
        if username in users and users[username]['password'] == password:
            return jsonify({'status': 'success', 'message': 'Login successful'})
        else:
            return jsonify({'status': 'error', 'message': 'Invalid credentials'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
