db.define_table('estudiantes',
 Field('id_estudiante', type="id", primary_key=True),
 Field('nombre', 'string', length=50, notnull=True),
 Field('edad', 'integer', notnull=True),
 Field('genero', 'string(1)', requires=IS_IN_SET(['M', 'F']))
)
    
db.define_table('salones',
 Field('id_salon', type="id", primary_key=True, autoincrement=True),
 Field('nombre', 'string', length=30, notnull=True)
)
    
db.define_table('materias',
  Field('id_materia', type="id", primary_key=True, autoincrement=True),
  Field('nombre', 'string', length=30, notnull=True)
)

db.define_table(
    'asistencias',
    Field('id_asistencia', type="id", primary_key=True, autoincrement=True),
    Field('id_estudiante', 'integer', db.estudiantes, notnull=True),
    Field('id_salon', 'integer', db.salones, notnull=True),
    Field('id_materia', 'integer', db.materias, notnull=True),
    Field('fecha', 'date', notnull=True),
    Field('asistio', 'boolean', notnull=True),
)