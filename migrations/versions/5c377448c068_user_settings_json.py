"""user settings json

Revision ID: 5c377448c068
Revises: 62170879a8e6
Create Date: 2021-04-10 13:58:33.189101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c377448c068'
down_revision = '62170879a8e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_settings_json', sa.String(256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_settings_json')
    # ### end Alembic commands ###
