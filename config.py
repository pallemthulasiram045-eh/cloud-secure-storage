import os

class Config:
    SECRET_KEY = "cloud_secure_storage_secret_key"

    # Upload folder
    UPLOAD_FOLDER = "static/uploads"

    # Maximum upload size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # MySQL Configuration
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "cloud_secure_storage"
