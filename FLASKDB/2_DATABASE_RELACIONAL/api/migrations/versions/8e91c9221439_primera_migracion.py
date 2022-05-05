"""primera migracion

Revision ID: 8e91c9221439
Revises: 
Create Date: 2022-05-05 12:15:44.465848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e91c9221439'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Mascotas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Juguetes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Text(), nullable=True),
    sa.Column('mascota_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mascota_id'], ['Mascotas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Propietarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Text(), nullable=True),
    sa.Column('mascota_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mascota_id'], ['Mascotas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Propietarios')
    op.drop_table('Juguetes')
    op.drop_table('Mascotas')
    # ### end Alembic commands ###
