"""new columns: users.login::str, unique not null

Revision ID: 72573e0d97e6
Revises: adf280d5b48f
Create Date: 2025-01-12 18:12:06.731089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = '72573e0d97e6'
down_revision: Union[str, None] = 'adf280d5b48f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('login', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'users', ['login'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'login')
    # ### end Alembic commands ###
