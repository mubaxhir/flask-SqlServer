"""Flask configuration variables."""
from os import urandom
server = 'localhost'
username = '<your_username>'
password = '<your_password>'
driver = 'ODBC+DRIVER+17+for+SQL+Server'aqsood_9211
database = 'SALES'
engine_stmt = 'mssql+pyodbc://{}:{}@{}/{}?driver={}'.format(username,
                                                            password,
                                                            server,
                                                            database,
                                                            driver)


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = urandom(24)
    # FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = 'production'

    # Database
    SQLALCHEMY_DATABASE_URI = engine_stmt
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
