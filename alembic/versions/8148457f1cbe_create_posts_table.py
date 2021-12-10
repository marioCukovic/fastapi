"""create posts table

Revision ID: 8148457f1cbe
Revises: 
Create Date: 2021-12-10 14:19:46.329964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8148457f1cbe"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
