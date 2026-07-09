from flask import Flask, render_template

app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = 'cloud_secure_storage_secret_key'


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Login Page
@app.route('/login')
def login():
    return render_template('login.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
