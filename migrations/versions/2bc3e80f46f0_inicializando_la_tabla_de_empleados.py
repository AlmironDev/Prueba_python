"""Inicializando la tabla de empleados

Revision ID: 2bc3e80f46f0
Revises: 
Create Date: 2024-09-25 10:52:58.951609

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2bc3e80f46f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('empleados', schema=None) as batch_op:
        batch_op.alter_column('edad',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('ciudad',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('salario',
               existing_type=mysql.DECIMAL(precision=10, scale=2),
               type_=sa.Float(),
               nullable=False)
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('empleados', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', mysql.VARCHAR(length=100), nullable=True))
        batch_op.alter_column('salario',
               existing_type=sa.Float(),
               type_=mysql.DECIMAL(precision=10, scale=2),
               nullable=True)
        batch_op.alter_column('ciudad',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('edad',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
