"""Descripción de la migración

Revision ID: b8f85faac907
Revises: b4ffbce744da
Create Date: 2024-09-25 13:34:22.368821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8f85faac907'
down_revision = 'b4ffbce744da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empresa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('ruc', sa.BIGINT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sectores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_empresa', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('empleados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_sector', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('edad', sa.Integer(), nullable=False),
    sa.Column('ciudad', sa.String(length=100), nullable=False),
    sa.Column('salario', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_sector'], ['sectores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empleados')
    op.drop_table('sectores')
    op.drop_table('empresa')
    # ### end Alembic commands ###
