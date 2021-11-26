"""add content column to posts table

Revision ID: a08d65a3293c
Revises: f51bc71fd2d6
Create Date: 2021-11-22 19:43:25.470905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a08d65a3293c'
down_revision = 'f51bc71fd2d6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
