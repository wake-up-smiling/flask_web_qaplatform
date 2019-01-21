"""empty message

Revision ID: b3b3264ecee5
Revises: 3332ed85a338
Create Date: 2019-01-21 00:50:41.017913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3b3264ecee5'
down_revision = '3332ed85a338'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'create_time')
    # ### end Alembic commands ###