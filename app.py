from flask import Flask, render_template

app = Flask(__name__)

# Secret Key for Session Management
app.config['SECRET_KEY'] = 'cloud_secure_storage_secret_key'


# ==========================
# Home Page
# ==========================
@app.route('/')
def home():
    return render_template('index.html')


# ==========================
# Login Page
# ==========================
@app.route('/login')
def login():
    return render_template('login.html')


# ==========================
# Register Page
# ==========================
@app.route('/register')
def register():
    return render_template('register.html')


# ==========================
# Run Application
# ==========================
if __name__ == '__main__':
    app.run(debug=True)
