"""empty message

Revision ID: 115d920f9b0c
Revises: baf68ebc2592
Create Date: 2021-07-17 09:37:22.048969

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '115d920f9b0c'
down_revision = 'baf68ebc2592'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events_invitations', 'status',
               existing_type=sa.Enum('invited', 'accepted', 'rejected', name='status'),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events_invitations', 'status',
               existing_type=sa.Enum('invited', 'accepted', 'rejected', name='status'),
               nullable=False)
    # ### end Alembic commands ###
