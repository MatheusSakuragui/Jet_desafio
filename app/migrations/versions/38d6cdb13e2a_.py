"""empty message

Revision ID: 38d6cdb13e2a
Revises: 4d06b630f36b
Create Date: 2024-01-03 15:51:52.870039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38d6cdb13e2a'
down_revision = '4d06b630f36b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venda',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.Column('produto_id', sa.Integer(), nullable=False),
    sa.Column('leilao_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.ForeignKeyConstraint(['leilao_id'], ['leilao.id'], ),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venda')
    # ### end Alembic commands ###
