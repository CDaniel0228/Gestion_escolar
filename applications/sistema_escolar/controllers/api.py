"""Module that provides API to add students."""
from repository.student_repository import StudentRepository
estudiantes_repository = StudentRepository(db)

def register():
    """Allows you to obtain student data"""
    response.headers['Access-Control-Allow-Origin'] = '*'  # API access permissions
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    id_student = request.post_vars.id
    name = request.post_vars.name
    age = request.post_vars.age
    gender = request.post_vars.gender

    if(estudiantes_repository.create(id_student, name, age, gender)): # database response
        return response.json({"message": "Successfully registered student"})
    else:
        return response.json({"message": "An error occurred in the registry"})
