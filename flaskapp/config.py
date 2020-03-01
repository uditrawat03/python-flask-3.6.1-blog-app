import os


class Config:
    # Secret Key
    SECRET_KEY = 'dfba6ca3b6aecf67cbcaecb4e6a65ec5'

    # Database setup
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # Mail setup
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'testuser@gmail.com'
    MAIL_PASSWORD = 'mytestpassword#'

    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
