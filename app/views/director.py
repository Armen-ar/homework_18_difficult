from flask_restx import Namespace, Resource

from app.dao.model.director import DirectorsSchema
from app.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    directors_schema = DirectorsSchema(many=True)

    def get(self):
        """Представление возвращает всех режиссёров"""

        return self.directors_schema.dump(director_service.get()), 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    director_schema = DirectorsSchema()

    def get(self, uid: int):
        """Представление возвращает режиссёра по id"""

        return self.director_schema.dump(director_service.get(uid)), 200
