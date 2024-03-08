"""version_inicial

Revision ID: e43eabe3fe01
Revises: 
Create Date: 2024-03-05 16:55:47.736435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e43eabe3fe01'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'estudiantes',
        sa.Column('id_estudiante', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String(50), nullable=False),
        sa.Column('edad', sa.Integer, nullable=False),
        sa.Column('genero', sa.String(1), nullable=False),
    )
    op.create_table(
        'salones',
        sa.Column('id_salon', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nombre', sa.String(30), nullable=False),
    )
    op.create_table(
        'materias',
        sa.Column('id_materia', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nombre', sa.String(30), nullable=False),
    )
    
    op.create_table(
        'asistencias',
        sa.Column('id_asistencia', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('id_estudiante', sa.Integer, sa.ForeignKey('estudiantes.id_estudiante'), nullable=False),
        sa.Column('id_salon', sa.Integer, sa.ForeignKey('salones.id_salon'), nullable=False),
        sa.Column('id_materia', sa.Integer, sa.ForeignKey('materias.id_materia'), nullable=False),
        sa.Column('fecha', sa.Date, nullable=False),
        sa.Column('asistio', sa.Boolean, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('estudiantes')
    op.drop_table('salones')
    op.drop_table('materias')
    op.drop_table('asistencias')
    
