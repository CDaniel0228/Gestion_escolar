from abc import ABC
from models.students_model import StudentModel


class FactoryStudent(ABC):
    def crear_salon(self, id: int, name: str, age: int, gender: str) -> StudentModel:
        return StudentModel(id, name, age, gender)
