from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get(self, mid, **kwargs):
        """Метод, который выводит все фильмы или фильмы по режиссёрам, жанрам и годам или фильм по id"""
        query = self.session.query(Movie)

        if mid:
            return query.get(mid)
        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(eval(f"Movie.{key}") == int(value))

        return query.all()

    def create(self, data):
        """Метод, который добавляет новый фильм"""
        movie = Movie(**data)

        with self.session.begin():
            self.session.add(movie)

        return movie

    def update(self, movie):
        """Метод, который обновляет полностью или частично данные фильма"""

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        """Метод, который удаляет данные фильма"""
        movie = self.get(mid)
        if not movie:
            return
        self.session.delete(movie)
        self.session.commit()
