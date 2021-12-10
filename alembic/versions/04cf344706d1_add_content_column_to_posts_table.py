"""add content column to posts table

Revision ID: 04cf344706d1
Revises: f26e1e9cea35
Create Date: 2021-12-10 08:13:18.496301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "04cf344706d1"
down_revision = "f26e1e9cea35"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
