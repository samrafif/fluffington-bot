"""fix weird alembic bug

Revision ID: 133cb8a9d265
Revises: 03a23b19e664
Create Date: 2022-05-10 22:33:16.787531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '133cb8a9d265'
down_revision = '03a23b19e664'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reminders',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('channel_id', sa.String(), nullable=True),
    sa.Column('guild_id', sa.String(), nullable=True),
    sa.Column('jump_url', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('expiration', sa.DateTime(), nullable=True),
    sa.Column('mentions', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reminders')
    # ### end Alembic commands ###