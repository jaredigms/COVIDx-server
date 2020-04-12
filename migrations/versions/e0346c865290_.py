"""empty message

Revision ID: e0346c865290
Revises: 00c3cef568ef
Create Date: 2020-04-12 15:32:37.709383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0346c865290'
down_revision = '00c3cef568ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('state_results',
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('positive', sa.Integer(), nullable=True),
    sa.Column('positiveScore', sa.Integer(), nullable=True),
    sa.Column('negativeScore', sa.Integer(), nullable=True),
    sa.Column('negativeRegularScore', sa.Integer(), nullable=True),
    sa.Column('commercialScore', sa.Integer(), nullable=True),
    sa.Column('grade', sa.String(length=5), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('negative', sa.Integer(), nullable=True),
    sa.Column('pending', sa.Integer(), nullable=True),
    sa.Column('hospitalizedCurrently', sa.Integer(), nullable=True),
    sa.Column('hospitalizedCumulative', sa.Integer(), nullable=True),
    sa.Column('inIcuCurrently', sa.Integer(), nullable=True),
    sa.Column('inIcuCumulative', sa.Integer(), nullable=True),
    sa.Column('onVentilatorCurrently', sa.Integer(), nullable=True),
    sa.Column('onVentilatorCumulative', sa.Integer(), nullable=True),
    sa.Column('recovered', sa.Integer(), nullable=True),
    sa.Column('lastUpdateEt', sa.String(length=50), nullable=True),
    sa.Column('checkTimeEt', sa.String(length=50), nullable=True),
    sa.Column('death', sa.Integer(), nullable=True),
    sa.Column('hospitalized', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('totalTestResults', sa.Integer(), nullable=True),
    sa.Column('posNeg', sa.Integer(), nullable=True),
    sa.Column('fips', sa.String(length=50), nullable=True),
    sa.Column('dateModified', sa.String(length=50), nullable=True),
    sa.Column('dateChecked', sa.String(length=50), nullable=True),
    sa.Column('notes', sa.String(length=100), nullable=True),
    sa.Column('hash', sa.String(length=50), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('hash'),
    sa.UniqueConstraint('hash')
    )
    op.create_table('location',
    sa.Column('location_id', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.String(length=50), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('location_id'),
    sa.UniqueConstraint('location_id')
    )
    op.add_column('users', sa.Column('date_join', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('img_link', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('sticky_lat', sa.Float(), nullable=True))
    op.add_column('users', sa.Column('sticky_lon', sa.Float(), nullable=True))
    op.alter_column('users', 'birth',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'birth',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.drop_column('users', 'sticky_lon')
    op.drop_column('users', 'sticky_lat')
    op.drop_column('users', 'img_link')
    op.drop_column('users', 'date_join')
    op.drop_table('location')
    op.drop_table('state_results')
    # ### end Alembic commands ###
