"""Running on k8s

Revision ID: ac1d5dc061b0
Revises: 
Create Date: 2019-09-18 18:56:50.870023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac1d5dc061b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AccountInfo',
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('account_email', sa.String(length=128), nullable=True),
    sa.Column('account_nickname', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('account_status', sa.String(length=8), nullable=True),
    sa.Column('account_create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('account_id')
    )
    op.create_index(op.f('ix_AccountInfo_account_email'), 'AccountInfo', ['account_email'], unique=True)
    op.create_index(op.f('ix_AccountInfo_account_nickname'), 'AccountInfo', ['account_nickname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_AccountInfo_account_nickname'), table_name='AccountInfo')
    op.drop_index(op.f('ix_AccountInfo_account_email'), table_name='AccountInfo')
    op.drop_table('AccountInfo')
    # ### end Alembic commands ###
