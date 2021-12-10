"""add foreign-key to posts table

Revision ID: 782fcda08d15
Revises: 1272416e0e1c
Create Date: 2021-12-10 08:44:43.161622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "782fcda08d15"
down_revision = "1272416e0e1c"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_user_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_user_fk", table_name="posts")
    op.drop_column("posts", column_name="owner_id")
    pass
