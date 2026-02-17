class Config:
    """
    Base configuration.
    """
    SECRET_KEY = 'your_secret_key'
    DEBUG = False
    TESTING = False
    API_URL = 'https://api.huggingface.co'

class DevelopmentConfig(Config):
    """
    Development configuration.
    """
    DEBUG = True
    ENV = 'development'
    # Add other development specific configurations here

class ProductionConfig(Config):
    """
    Production configuration.
    """
    ENV = 'production'
    # Add other production specific configurations here

class TestingConfig(Config):
    """
    Testing configuration.
    """
    TESTING = True
    ENV = 'testing'
    # Add other testing specific configurations here
    # Example:
    # API_URL = 'https://testing-api.huggingface.co'