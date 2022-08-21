from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get(self, gid=None) -> list[dict]:
        """Метод, который выводит все жанры или жанр по id"""

        return self.dao.get(gid)

