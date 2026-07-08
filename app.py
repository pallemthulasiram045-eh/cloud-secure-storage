from flask import Flask

app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = 'cloud_secure_storage_secret_key'


@app.route('/')
def home():
    return """
    <h1>☁️ Cloud Secure Storage</h1>
    <h3>Welcome to the Cloud Secure Storage Application</h3>
    <p>This project is currently under development.</p>
    """


if __name__ == '__main__':
    app.run(debug=True)
