"""empty message

Revision ID: 95ec6235ad76
Revises: 
Create Date: 2022-05-26 04:41:29.348108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95ec6235ad76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coletas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rssi', sa.Float(), nullable=True),
    sa.Column('orientacao', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('ap_fonte', sa.Integer(), nullable=True),
    sa.Column('xp', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('elementos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(), nullable=True),
    sa.Column('mac', sa.String(), nullable=True),
    sa.Column('posicao_x', sa.Float(), nullable=True),
    sa.Column('posicao_y', sa.Float(), nullable=True),
    sa.Column('posicao_z', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('elementos')
    op.drop_table('coletas')
    # ### end Alembic commands ###
