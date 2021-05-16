"""create test table

Revision ID: b19485f26143
Revises: 
Create Date: 2021-04-06 22:49:44.712456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b19485f26143'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_info',
        sa.Column('user_id',sa.VARCHAR(32),primary_key=True,nullable=False),
        sa.Column('user_name',sa.VARCHAR(32),nullable=False),
        sa.Column('user_email',sa.VARCHAR(32),nullable=False),
        sa.Column('user_password',sa.VARCHAR(64),nullable=False),
        sa.Column('user_image',sa.VARCHAR(32),nullable=True),
        sa.Column('create_time_stamp',sa.DateTime(),nullable=False),
        sa.Column('update_time_stamp',sa.DateTime(),nullable=False),
        )
    op.create_table('room_info',
        sa.Column('user_id',sa.VARCHAR(32),primary_key=True,nullable=False),
        sa.Column('room_id',sa.VARCHAR(32),nullable=False),
        sa.Column('room_title',sa.VARCHAR(32),nullable=False),
        sa.Column('create_time_stamp',sa.DateTime(),nullable=False),
        sa.Column('update_time_stamp',sa.DateTime(),nullable=False),
        )


def downgrade():
    op.drop_table('user_info')
    op.drop_table('room_info')
