"""create contracts

Revision ID: e26113374137
Revises: 22d39ca864b9
Create Date: 2024-07-09 16:15:21.171397

"""

import json
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Table

from src.models import Base

# revision identifiers, used by Alembic.
revision: str = "e26113374137"
down_revision: Union[str, None] = "22d39ca864b9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    path = "alembic/fixtures/contracts.json"
    contracts_table = Table("contracts", Base.metadata)
    with open(path) as file:
        data = json.load(file)
    op.bulk_insert(contracts_table, data["contracts"])


def downgrade() -> None:
    connection = op.get_bind()
    contracts_table = Table("contracts", Base.metadata)
    connection.execute(contracts_table.delete().where())
