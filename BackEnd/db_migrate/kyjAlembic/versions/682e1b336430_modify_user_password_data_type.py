"""modify user_password data type

Revision ID: 682e1b336430
Revises: b19485f26143
Create Date: 2021-05-29 17:16:37.225633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '682e1b336430'
down_revision = 'b19485f26143'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('user_info', 'user_password',existing_type=sa.VARCHAR(length=32), type_=sa.String(length=64))



def downgrade():
    op.alter_column('user_info', 'user_password',existing_type=sa.VARCHAR(length=64), type_=sa.String(length=32))
