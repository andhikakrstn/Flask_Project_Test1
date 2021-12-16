"""buat tabel gambar

Revision ID: f36703bcebf4
Revises: e3cf6d5dfaf1
Create Date: 2021-12-03 12:13:10.342121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f36703bcebf4'
down_revision = 'e3cf6d5dfaf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gambar',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('judul', sa.String(length=50), nullable=False),
    sa.Column('pathname', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gambar')
    # ### end Alembic commands ###
