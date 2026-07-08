from flask import Flask, render_template

app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = 'cloud_secure_storage_secret_key'


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
