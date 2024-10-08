"""Descripción de la migración

Revision ID: 02aa7297f365
Revises: 46c743359093
Create Date: 2024-09-25 12:55:35.068184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02aa7297f365'
down_revision = '46c743359093'
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
