"""add last few columns to post table

Revision ID: ced1a71df97a
Revises: 782fcda08d15
Create Date: 2021-12-10 08:53:01.201286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ced1a71df97a"
down_revision = "782fcda08d15"
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
