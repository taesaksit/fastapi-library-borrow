"""change name to lowercase

Revision ID: 098b7ec7412c
Revises: 15248609d289
Create Date: 2025-07-26 00:17:09.695068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '098b7ec7412c'
down_revision: Union[str, Sequence[str], None] = '15248609d289'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
