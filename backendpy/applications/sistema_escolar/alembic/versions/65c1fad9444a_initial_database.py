"""initial database

Revision ID: 65c1fad9444a
Revises: 
Create Date: 2024-03-11 11:00:54.547715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65c1fad9444a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

""" 
In this revision the database tables are
created as well as some test data is inserted
"""
def upgrade() -> None:
    students_table = op.create_table(
        'estudiantes',
        sa.Column('id_estudiante', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String(50), nullable=False),
        sa.Column('edad', sa.Integer, nullable=False),
        sa.Column('genero', sa.String(1), nullable=False),
    )
    salons_table = op.create_table(
        'salones',
        sa.Column('id_salon', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nombre', sa.String(30), nullable=False),
    )
    subjects_table = op.create_table(
        'materias',
        sa.Column('id_materia', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nombre', sa.String(30), nullable=False),
    )
    
    attendance_table = op.create_table(
        'asistencias',
        sa.Column('id_asistencia', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('id_estudiante', sa.Integer, sa.ForeignKey('estudiantes.id_estudiante'), nullable=False),
        sa.Column('id_salon', sa.Integer, sa.ForeignKey('salones.id_salon'), nullable=False),
        sa.Column('id_materia', sa.Integer, sa.ForeignKey('materias.id_materia'), nullable=False),
        sa.Column('fecha', sa.Date, nullable=False),
        sa.Column('asistio', sa.Boolean, nullable=True),
    )
    op.bulk_insert(
        students_table,
        [
            {"id_estudiante": 1, "nombre": "John Smith", "edad": 15, "genero": "M"},
            {"id_estudiante": 2, "nombre": "Emma Johnson", "edad": 20, "genero": "F"},
            {"id_estudiante": 3, "nombre": "Michael Brown", "edad": 25, "genero": "M"},
            {"id_estudiante": 4, "nombre": "Sophia Miller", "edad": 22, "genero": "F"},
            {"id_estudiante": 5, "nombre": "Daniel Davis", "edad": 28, "genero": "M"},
            {"id_estudiante": 6, "nombre": "Olivia Wilson", "edad": 19, "genero": "F"},
            {"id_estudiante": 7, "nombre": "Matthew Taylor", "edad": 26, "genero": "M"},
            {"id_estudiante": 8, "nombre": "Ava Martinez", "edad": 23, "genero": "F"},
            {"id_estudiante": 9, "nombre": "Ethan Anderson", "edad": 21, "genero": "M"},
            {"id_estudiante": 10, "nombre": "Mia Thomas", "edad": 24, "genero": "F"},
        ],  
    )
    
    op.bulk_insert(
        salons_table,
        [
            {"nombre": "Salon A"},
            {"nombre": "Salon B"},
            {"nombre": "Salon C"},
            {"nombre": "Salon D"},
            {"nombre": "Salon E"},
            {"nombre": "Salon F"},
            {"nombre": "Salon G"},
            {"nombre": "Salon H"},
            {"nombre": "Salon I"},
            {"nombre": "Salon J"},
        ],
    )
    op.bulk_insert(
        subjects_table,
        [
            {"nombre": "Matematicas"},
            {"nombre": "Historia"},
            {"nombre": "Ciencias"},
            {"nombre": "Literatura"},
            {"nombre": "Ingles"},
            {"nombre": "Programacion"},
            {"nombre": "Arte"},
            {"nombre": "Educación Fisica"},
            {"nombre": "Química"},
            {"nombre": "Biologia"},
        ],
    )
    # 10 attendance lists are created
    for i in range(1, 11):
        for j in range(1, 11):
            op.bulk_insert(
                attendance_table,
                [
                    {"id_estudiante": j,"id_salon": i, "id_materia": i, "fecha":op.inline_literal("2024-03-15")},
                ],
                multiinsert=False,
            )


def downgrade() -> None:
    op.drop_table('estudiantes')
    op.drop_table('salones')
    op.drop_table('materias')
    op.drop_table('asistencias')
    