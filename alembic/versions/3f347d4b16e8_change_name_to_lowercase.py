"""change name to lowercase

Revision ID: 3f347d4b16e8
Revises: 098b7ec7412c
Create Date: 2025-07-26 00:21:59.265936

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f347d4b16e8'
down_revision: Union[str, Sequence[str], None] = '098b7ec7412c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
