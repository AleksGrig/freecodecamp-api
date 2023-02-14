"""create posts table

Revision ID: 5ef04bc16a1f
Revises: 84624fba9734
Create Date: 2023-02-13 12:53:27.923734

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import true


# revision identifiers, used by Alembic.
revision = '5ef04bc16a1f'
down_revision = '84624fba9734'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(30), nullable=False),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('content', sa.String(150), nullable=False),
                    sa.Column('published', sa.Boolean(), nullable=False, server_default=true()),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
                  )
    op.create_foreign_key('post_user_fk',
                          source_table='posts',
                          referent_table='users',
                          local_cols=['owner_id'],
                          remote_cols=['id'],
                          ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name='posts', type_='foreignkey')
    op.drop_table('posts')
