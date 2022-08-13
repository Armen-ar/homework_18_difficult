from flask import request, make_response
from flask_restx import Namespace, Resource

from app.dao.model.movie import MoviesSchema
from app.implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    movie_schema = MoviesSchema()
    movies_schema = MoviesSchema(many=True)

    def get(self):
        """Представление возвращает все фильмы или фильмы по режиссёрам, жанрам и годам"""

        movies = self.movies_schema.dump(movie_service.get_movies(**request.args))

        return movies, 200

    def post(self):
        """Представление добавляет данные о новом фильме"""
        new_movie = movie_service.create(request.json)
        resp = make_response("", 201)
        resp.headers['Location'] = f"{movie_ns.path}/{new_movie.id}"

        return resp


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    movie_schema = MoviesSchema()

    def get(self, uid: int):
        """Представление возвращает фильм по id"""

        return self.movie_schema.dump(movie_service.get_movies(uid)), 200

    def put(self, uid: int):
        """Представление обновляет данные фильма по id"""

        return self.movie_schema.dump(movie_service.update(uid, request.json)), 204

    def patch(self, uid: int):
        """Представление обновляет частично данные фильма по id"""

        return self.movie_schema.dump(movie_service.update_partial(uid, request.json)), 204

    def delete(self, uid: int):
        """Представление удаляет данные фильма по id"""
        movie_service.delete(uid)

        return "", 204
