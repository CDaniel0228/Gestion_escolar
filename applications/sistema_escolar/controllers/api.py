from repository.student_repository import StudentRepository
estudiantes_repository = StudentRepository(db)

def register():
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'  # Reemplaza con la URL de tu frontend
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    id = request.post_vars.id
    name = request.post_vars.name
    age = request.post_vars.age
    gender = request.post_vars.gender
    estudiante_id = estudiantes_repository.create(id, name, age, gender)
    return response.json({'message': 'Estudiante registrado exitosamente'})