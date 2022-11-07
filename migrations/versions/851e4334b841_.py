"""empty message

Revision ID: 851e4334b841
Revises: 23400ccdeb8f
Create Date: 2022-11-07 11:17:37.493380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '851e4334b841'
down_revision = '23400ccdeb8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('restaurant_name', sa.String(), nullable=True),
    sa.Column('meal', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('breakfast', sa.Column('menu_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'breakfast', 'menu', ['menu_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'breakfast', type_='foreignkey')
    op.drop_column('breakfast', 'menu_id')
    op.drop_table('menu')
    # ### end Alembic commands ###
