from abc import ABC 
from models.classrooms_model import Classroom
class FactorySalon(ABC):
    _instance = None
    _cache = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def crear_salon(self, name: str) -> Classroom:
        if id not in self._cache:
            self._cache[id] = Classroom(name)
        return self._cache[id]
