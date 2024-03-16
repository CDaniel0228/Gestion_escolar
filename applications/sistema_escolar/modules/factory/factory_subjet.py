from abc import ABC 
from models.subjets_model import Subjet
class FactoryMateria(ABC):
    _instance: 'FactorySubjet' = None
    _cache: dict = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def crear_materia(self, nombre: str) -> Subjet:
        if id not in self._cache:
            self._cache[id] = Subjet(nombre)
        return self._cache[id]
