"""add users table

Revision ID: f205c90db55f
Revises: 04cf344706d1
Create Date: 2021-12-10 08:18:35.214136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f205c90db55f"
down_revision = "04cf344706d1"
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
