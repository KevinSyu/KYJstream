"""change primary key for room_info

Revision ID: ee725240d749
Revises: 682e1b336430
Create Date: 2021-06-08 21:22:27.888810

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'ee725240d749'
down_revision = '682e1b336430'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()

    if 'room_info' in tables:
        op.drop_table('room_info')

    op.create_table('room_info',
    sa.Column('room_id',sa.VARCHAR(32),primary_key=True,nullable=False),
    sa.Column('user_id',sa.VARCHAR(32),nullable=False),
    sa.Column('room_title',sa.VARCHAR(32),nullable=False),
    sa.Column('create_time_stamp',sa.DateTime(),nullable=False),
    sa.Column('update_time_stamp',sa.DateTime(),nullable=False),
    )

def downgrade():
    pass