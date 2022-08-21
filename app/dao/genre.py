from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get(self, gid=None) -> list[dict]:
        """Метод, который выводит все жанры или жанр по id"""
        query = self.session.query(Genre)
        if gid:
            return query.get(gid)
        else:
            return query.all()
