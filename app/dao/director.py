from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get(self, did=None) -> list[dict]:
        """Метод, который выводит всех режиссёров или режиссёра по id"""
        query = self.session.query(Director)
        if did:
            return query.get(did)
        else:
            return query.all()
