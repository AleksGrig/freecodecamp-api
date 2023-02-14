"""create users table

Revision ID: 84624fba9734
Revises: 
Create Date: 2023-02-13 12:47:03.024195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84624fba9734'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                  sa.Column('id', sa.Integer(), nullable=False),
                  sa.Column('email', sa.String(30), nullable=False),
                  sa.Column('password', sa.String(150), nullable=False),
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                  sa.PrimaryKeyConstraint('id'),
                  sa.UniqueConstraint('email')
                )


def downgrade() -> None:
    op.drop_table('users')
