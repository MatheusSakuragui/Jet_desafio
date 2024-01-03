"""Description of your changes

Revision ID: bd9c53beca95
Revises: b495250c4ad5
Create Date: 2024-01-02 13:54:47.130210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd9c53beca95'
down_revision = 'b495250c4ad5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leilao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_futura', sa.DateTime(timezone=80), nullable=False),
    sa.Column('data_visitacao', sa.DateTime(timezone=80), nullable=False),
    sa.Column('detalhes', sa.String(length=120), nullable=False),
    sa.Column('qtd_produtos', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('EM ABERTO', 'EM ANDAMENTO', 'FINALIZADO', name='status_enum'), server_default='EM ABERTO', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leilao')
    # ### end Alembic commands ###
