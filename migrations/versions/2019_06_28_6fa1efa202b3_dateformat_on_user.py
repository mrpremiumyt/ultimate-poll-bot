"""Dateformat on user

Revision ID: 6fa1efa202b3
Revises: 381ef6581a03
Create Date: 2019-06-28 13:16:29.691281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6fa1efa202b3"
down_revision = "381ef6581a03"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "poll",
        "european_date_format",
        existing_type=sa.BOOLEAN(),
        server_default=None,
        existing_nullable=False,
    )
    op.alter_column(
        "poll_option",
        "is_date",
        existing_type=sa.BOOLEAN(),
        server_default=None,
        existing_nullable=False,
    )
    op.add_column(
        "user",
        sa.Column(
            "european_date_format", sa.Boolean(), server_default="false", nullable=False
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "european_date_format")
    op.alter_column(
        "poll_option",
        "is_date",
        existing_type=sa.BOOLEAN(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )
    op.alter_column(
        "poll",
        "european_date_format",
        existing_type=sa.BOOLEAN(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
