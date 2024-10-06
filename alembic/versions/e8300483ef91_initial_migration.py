"""Initial migration

Revision ID: e8300483ef91
Revises: 
Create Date: 2024-10-04 15:11:14.788964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8300483ef91'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(), nullable=True))
    op.add_column('users', sa.Column('avatar_url', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password_reset_token', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password_reset_token_expiry', sa.String(), nullable=True))
    op.add_column('users', sa.Column('google_id', sa.String(), nullable=True))
    op.add_column('users', sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('false'), nullable=True))
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), server_default=sa.text('false'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_verified')
    op.drop_column('users', 'is_deleted')
    op.drop_column('users', 'google_id')
    op.drop_column('users', 'password_reset_token_expiry')
    op.drop_column('users', 'password_reset_token')
    op.drop_column('users', 'avatar_url')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
