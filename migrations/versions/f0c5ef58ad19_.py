"""empty message

Revision ID: f0c5ef58ad19
Revises: 80d2754fb939
Create Date: 2016-12-03 22:23:20.973696

"""

# revision identifiers, used by Alembic.
revision = 'f0c5ef58ad19'
down_revision = '80d2754fb939'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('path', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], [u'user.id'], name=u'files_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'files_pkey')
    )
    ### end Alembic commands ###
