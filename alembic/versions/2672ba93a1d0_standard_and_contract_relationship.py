"""standard and contract relationship

Revision ID: 2672ba93a1d0
Revises: d331d0b5e4b0
Create Date: 2024-07-09 13:34:27.403857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2672ba93a1d0'
down_revision: Union[str, None] = 'd331d0b5e4b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contracts', sa.Column('standard_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'contracts', 'standards', ['standard_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contracts', type_='foreignkey')
    op.drop_column('contracts', 'standard_id')
    # ### end Alembic commands ###
