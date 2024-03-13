from gluon import *

class ControlAsistencia:      
    def __init__(self, db):
        self.db = db
        self.estudiante = db.estudiantes
        self.salon = db.salones
        self.materia = db.materias
        self.asistencia = db.asistencias
        
    def seguimiento_asistencia(self, options):
        query = (
        (self.asistencia.id_estudiante == self.estudiante.id) &
        (self.asistencia.id_salon == self.salon.id) &
        (self.asistencia.id_materia == self.materia.id)
        )   
        grid = SQLFORM.grid(
            query,
            user_signature=False,
            fields=[
                self.estudiante.nombre,
                self.salon.nombre,
                self.materia.nombre,
                self.asistencia.fecha,
                self.asistencia.asistio,
                
            ],
            headers={
                'estudiantes.nombre': 'Estudiantes',
                'salones.nombre': 'Salon',
                'materias.nombre': 'Materia',
                'asistencias.asistio': '',
            },
            orderby=None,
            create=False,
            deletable=False,
            editable=False,
            details=False,
            paginate=10,
            csv=False,
            searchable=False,
            sortable=False,
            links = [dict(
                header='Asistencia', 
                body=lambda row: SELECT(options,  
                                        value=options[1] if row.asistencias.asistio else options[0], 
                                        _onchange='registrarCambioAsistencia(this.value, {0})'.format(row.asistencias.id)))]
        )
        
        current.response.files.append(URL('static', 'js/asistencia.js'))
        return DIV(grid)