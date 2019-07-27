"""user table

Revision ID: 5ccb3836817a
Revises: 7a0fcd93e0f5
Create Date: 2019-05-15 10:20:06.222200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ccb3836817a'
down_revision = '7a0fcd93e0f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone_number', sa.String(length=16), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_index('ix_UserInfo_email', table_name='UserInfo')
    op.drop_index('ix_UserInfo_phone_number', table_name='UserInfo')
    op.drop_index('ix_UserInfo_username', table_name='UserInfo')
    op.drop_table('UserInfo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserInfo',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=16), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_UserInfo_username', 'UserInfo', ['username'], unique=1)
    op.create_index('ix_UserInfo_phone_number', 'UserInfo', ['phone_number'], unique=1)
    op.create_index('ix_UserInfo_email', 'UserInfo', ['email'], unique=1)
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
