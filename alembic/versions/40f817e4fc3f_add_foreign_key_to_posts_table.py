"""add foreign key to posts table

Revision ID: 40f817e4fc3f
Revises: b907da9712f4
Create Date: 2021-11-22 19:55:11.856361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40f817e4fc3f'
down_revision = 'b907da9712f4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', 
                          referent_table='users', local_cols=['user_id'], 
                          remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass
