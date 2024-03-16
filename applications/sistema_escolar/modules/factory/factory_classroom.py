from abc import ABC 
from models.classrooms_model import Classroom
class FactoryClassroom(ABC):
    _instance: 'FactoryClassroom' = None
    _cache: dict = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create_classroom(self, name: str) -> Classroom:
        if id not in self._cache:
            self._cache[id] = Classroom(name)
        return self._cache[id]
