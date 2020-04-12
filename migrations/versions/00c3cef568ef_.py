"""empty message

Revision ID: 00c3cef568ef
Revises: ed02b69c4934
Create Date: 2020-04-12 13:28:15.051782

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '00c3cef568ef'
down_revision = 'ed02b69c4934'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('record_id', table_name='state_results')
    op.create_unique_constraint(None, 'state_results', ['hash'])
    op.drop_column('state_results', 'record_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('state_results', sa.Column('record_id', mysql.VARCHAR(length=50), nullable=False))
    op.drop_constraint(None, 'state_results', type_='unique')
    op.create_index('record_id', 'state_results', ['record_id'], unique=True)
    # ### end Alembic commands ###