from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        seed_data()

    from app.routes import main
    app.register_blueprint(main)

    return app

def seed_data():
    from app.models import User
    if not User.query.first():
        db.session.add(User(username='admin'))
        db.session.commit()