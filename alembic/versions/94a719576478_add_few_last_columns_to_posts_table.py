"""add few last columns to posts table

Revision ID: 94a719576478
Revises: 9a694f26f38d
Create Date: 2021-12-10 14:48:59.559156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "94a719576478"
down_revision = "9a694f26f38d"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    ),
    op.add_column(
        "posts",
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )

    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
