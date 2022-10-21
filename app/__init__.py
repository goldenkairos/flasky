from flask import Flask

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    from .routes.breakfast import breakfast_bp
    app.register_blueprint(breakfast_bp)
    return app