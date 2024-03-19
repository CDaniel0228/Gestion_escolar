"""Module that provides CRUD functions for students."""
class StudentRepository:
    def __init__(self, db):
        """
        Initialization of the class for connection
        to the students table of the database
        """
        self.db = db 
        self.estudiante = db.estudiantes 

    def create(self, id_student:int, name:str, age:int, gender:str) -> bool:
        """Allows you to add information about new students"""
        try:
            self.estudiante.insert(
                id_estudiante=id_student, nombre=name, edad=age, genero=gender
            )
            return True
        except Exception as e:
            return False

    def update(self, id_student:int, name:str, age:int, gender:str) -> bool:
        """Allows you to update information about a student."""
        try:
            registro = self.db(self.estudiante.id == id_student).select().first()
            if registro:
                registro.update_record(nombre=name, edad=age, gender=gender)
            return registro
        except Exception as e:
            return False

    def get_id_studens(self, id_student: int):
        """Get a record by your ID"""
        return self.db(self.estudiante.id == id_student).select().first()

    def get_all_students(self):
        """Get all records"""
        return self.db(self.estudiante).select()
