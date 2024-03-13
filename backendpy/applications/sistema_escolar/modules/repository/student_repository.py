class StudentRepository:
    def __init__(self, db):
        self.db = db
        self.estudiante = db.estudiantes

    def create(self, id, name, age, gender):
        try:
            self.estudiante.insert(id_estudiante=id, nombre=name, edad=age, genero=gender)
        except Exception as e:
            print(f"Error al insertar estudiante: {e}")
        return "nodo"

    def update(self, id, name, age, gender):
        try:
            registro = self.db(self.estudiante.id == id).select().first()
            if registro:
                registro.update_record(nombre=nombre, edad=edad)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al insertar estudiante: {e}")
        return "nodo"
    
    def obtener_registro_por_id(self, id):
        # Obtener un registro por su ID
        return self.db(self.estudiante.id == id).select().first()

    def obtener_todos_los_registros(self):
        # Obtener todos los registros de la tabla
        return self.db(self.estudiante).select()
            
            
        