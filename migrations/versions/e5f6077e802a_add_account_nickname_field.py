"""Add account_nickname field

Revision ID: e5f6077e802a
Revises: 97c7c5af3e64
Create Date: 2019-09-15 17:16:17.581768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5f6077e802a'
down_revision = '97c7c5af3e64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('AccountInfo', sa.Column('account_nickname', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_AccountInfo_account_nickname'), 'AccountInfo', ['account_nickname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_AccountInfo_account_nickname'), table_name='AccountInfo')
    op.drop_column('AccountInfo', 'account_nickname')
    # ### end Alembic commands ###