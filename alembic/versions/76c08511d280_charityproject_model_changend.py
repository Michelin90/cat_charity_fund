"""CharityProject model changend

Revision ID: 76c08511d280
Revises: 37145849d34e
Create Date: 2023-11-13 18:49:50.485560

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '76c08511d280'
down_revision = '37145849d34e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###
