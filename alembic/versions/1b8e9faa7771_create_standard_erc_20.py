"""create standard erc-20

Revision ID: 1b8e9faa7771
Revises: e26113374137
Create Date: 2024-07-09 16:26:15.272486

"""

import json
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Table

from src.models import Base

# revision identifiers, used by Alembic.
revision: str = "1b8e9faa7771"
down_revision: Union[str, None] = "e26113374137"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    path = "alembic/fixtures/standards.json"
    standards_table = Table("standards", Base.metadata)
    functions_table = Table("functions", Base.metadata)
    function__standard_table = Table("function__standard", Base.metadata)
    with open(path) as file:
        data = json.load(file)
    for standard_data in data["standard"]:
        functions = standard_data.pop("functions")
        op.bulk_insert(standards_table, [standard_data])
        op.bulk_insert(functions_table, functions)
        op.bulk_insert(
            function__standard_table,
            rows=[
                {"standard_id": standard_data["id"], "function_id": function["id"]}
                for function in functions
            ],
        )


def downgrade() -> None:
    connection = op.get_bind()
    standards_table = Table("standards", Base.metadata)
    functions_table = Table("functions", Base.metadata)
    function__standard_table = Table("function__standard", Base.metadata)
    connection.execute(standards_table.delete().where())
    connection.execute(functions_table.delete().where())
    connection.execute(function__standard_table.delete().where())