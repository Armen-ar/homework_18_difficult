from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get(self, did=None):
        """Метод, который выводит всех режиссёров или режиссёра по id"""

        return self.dao.get(did)

