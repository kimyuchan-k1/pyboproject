"""empty message

Revision ID: 32eae38a54b0
Revises: 2a2c919ede08
Create Date: 2024-05-27 23:56:08.497592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32eae38a54b0'
down_revision = '2a2c919ede08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
