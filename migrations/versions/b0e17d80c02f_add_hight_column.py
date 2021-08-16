"""add hight column

Revision ID: b0e17d80c02f
Revises: 
Create Date: 2021-08-17 01:45:14.760022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0e17d80c02f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('AOA', sa.Column('height', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('AOA', 'height')
    # ### end Alembic commands ###
