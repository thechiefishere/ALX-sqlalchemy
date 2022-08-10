"""empty message

Revision ID: 856e80b18a04
Revises: 356b1cc844ae
Create Date: 2022-08-10 22:06:17.662711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '856e80b18a04'
down_revision = '356b1cc844ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('completed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'completed')
    # ### end Alembic commands ###
