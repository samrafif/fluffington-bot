"""added prefix column to guild table

Revision ID: bf16eb5f1f76
Revises: b57e8d62de3c
Create Date: 2021-09-05 19:55:33.336497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf16eb5f1f76'
down_revision = 'b57e8d62de3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guilds', sa.Column('prefix', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('guilds', 'prefix')
    # ### end Alembic commands ###
