"""add column status to borrows

Revision ID: 15248609d289
Revises: c25446498740
Create Date: 2025-07-26 00:05:00.438296
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "15248609d289"
down_revision: Union[str, Sequence[str], None] = "c25446498740"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Enum type
borrow_status_enum = sa.Enum(
    "returned", "borrowed", "waiting_approve", name="borrowstatus"
)


def upgrade() -> None:
    # 1) Create Enum type first
    borrow_status_enum.create(op.get_bind(), checkfirst=True)

    # 2) Add column using this Enum type
    op.add_column(
        "borrows",
        sa.Column(
            "status",
            borrow_status_enum,
            nullable=False,
            server_default="borrowed",  # ให้ค่า default ป้องกัน NOT NULL error
        ),
    )


def downgrade() -> None:
    # 1) Drop column first
    op.drop_column("borrows", "status")

    # 2) Drop Enum type
    borrow_status_enum.drop(op.get_bind(), checkfirst=True)
