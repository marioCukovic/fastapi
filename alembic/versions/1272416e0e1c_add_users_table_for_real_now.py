"""add users table for real now

Revision ID: 1272416e0e1c
Revises: be6b55be4d3b
Create Date: 2021-12-10 08:43:11.204383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1272416e0e1c"
down_revision = "be6b55be4d3b"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
