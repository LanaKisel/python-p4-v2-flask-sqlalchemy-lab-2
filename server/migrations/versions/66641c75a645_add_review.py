"""add review

Revision ID: 66641c75a645
Revises: 19a48c2c83a8
Create Date: 2024-03-15 14:56:21.414144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66641c75a645'
down_revision = '19a48c2c83a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('item_is', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_reviews_customer_id_customers')),
    sa.ForeignKeyConstraint(['item_is'], ['items.id'], name=op.f('fk_reviews_item_is_items')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
