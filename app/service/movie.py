from typing import Tuple, Optional

from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_movies(self, mid=None, **kwargs):
        """Метод, который выводит все фильмы или фильмы по режиссёрам, жанрам и годам или фильм по id"""

        return self.dao.get(mid, **kwargs)

    def create(self, data: dict) -> dict:
        """Метод, который добавляет данные о новом фильме"""

        return self.dao.create(data)

    def update(self, mid: int, data: dict) -> Tuple:
        """Метод, который обновляет полностью данные фильма"""
        movie = self.get_movies(mid)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.dao.update(movie)

        return movie, 200

    def update_partial(self, mid: int, data: dict) -> Tuple:
        """Метод, который обновляет частично данные фильма"""
        movie = self.get_movies(mid)

        if 'title' in data:
            movie.title = data['title']
        elif 'description' in data:
            movie.description = data['description']
        elif 'trailer' in data:
            movie.trailer = data['trailer']
        elif 'year' in data:
            movie.year = data['year']
        elif 'rating' in data:
            movie.rating = data['rating']
        elif 'genre_id' in data:
            movie.genre_id = data['genre_id']
        elif 'director_id' in data:
            movie.director_id = data['director_id']
        self.dao.update(movie)

        return movie, 204

    def delete(self, mid: int):
        """Метод, который удаляет данные фильма"""
        self.dao.delete(mid)
