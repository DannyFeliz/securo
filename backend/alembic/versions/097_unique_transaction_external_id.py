"""dedupe transactions by account external id and date

Revision ID: 097
Revises: 096
Create Date: 2026-07-09
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "097"
down_revision: Union[str, None] = "096"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS ux_transactions_account_external_date "
        "ON transactions (account_id, external_id, date) "
        "WHERE external_id IS NOT NULL"
    )


def downgrade() -> None:
    op.drop_index("ux_transactions_account_external_date", table_name="transactions")
