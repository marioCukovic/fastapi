"""add foreign key to posts table

Revision ID: 9a694f26f38d
Revises: 6a9aebb54c6c
Create Date: 2021-12-10 14:46:31.432199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9a694f26f38d"
down_revision = "6a9aebb54c6c"
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
