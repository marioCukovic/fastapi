"""add content column to posts table

Revision ID: 9e2ef813347e
Revises: 8148457f1cbe
Create Date: 2021-12-10 14:40:20.299321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9e2ef813347e"
down_revision = "8148457f1cbe"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
