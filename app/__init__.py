from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS support

    # Register blueprints for the different routes
    from .routes.home import home
    from .routes.text import text
    from .routes.image import image
    from .routes.video import video
    from .routes.audio import audio

    app.register_blueprint(home)
    app.register_blueprint(text)
    app.register_blueprint(image)
    app.register_blueprint(video)
    app.register_blueprint(audio)

    return app
