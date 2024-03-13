from abc import ABC 
from models.students_model import StudentModel
class FactoryEstudiante(ABC):    
    def crear_salon(self, name, age, gender) -> StudentModel:
        return StudentModel(name, age, gender)
