"""empty message

Revision ID: 22519132286a
Revises: 979e274ba2ae
Create Date: 2016-06-23 18:11:50.516310

"""

# revision identifiers, used by Alembic.
revision = '22519132286a'
down_revision = '979e274ba2ae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('submissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_id', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['model_id'], ['model_grids.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_submissions_model_id'), 'submissions', ['model_id'], unique=False)
    op.create_index(op.f('ix_model_grids_id'), 'model_grids', ['id'], unique=False)
    op.create_index(op.f('ix_model_grids_updated_at'), 'model_grids', ['updated_at'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_model_grids_updated_at'), table_name='model_grids')
    op.drop_index(op.f('ix_model_grids_id'), table_name='model_grids')
    op.drop_index(op.f('ix_submissions_model_id'), table_name='submissions')
    op.drop_table('submissions')
    ### end Alembic commands ###
