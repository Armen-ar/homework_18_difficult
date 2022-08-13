from flask_restx import Namespace, Resource

from app.dao.model.genre import GenresSchema
from app.implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    genres_schema = GenresSchema(many=True)

    def get(self):
        """Представление возвращает все жанры"""

        return self.genres_schema.dump(genre_service.get()), 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    genre_schema = GenresSchema()

    def get(self, uid: int):
        """Представление возвращает жанр по id"""

        return self.genre_schema.dump(genre_service.get(uid)), 200
