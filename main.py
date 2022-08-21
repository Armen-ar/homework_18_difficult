from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.director import director_ns
from app.views.genre import genre_ns
from app.views.movie import movie_ns


def create_app(config_object) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application) -> None:
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run()
