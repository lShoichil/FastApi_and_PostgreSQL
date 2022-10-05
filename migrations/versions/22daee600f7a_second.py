"""Second

Revision ID: 22daee600f7a
Revises: abc50f3d50d9
Create Date: 2022-10-06 04:15:22.493368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22daee600f7a'
down_revision = 'abc50f3d50d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('microlog_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_microlog_posts_id'), 'microlog_posts', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_microlog_posts_id'), table_name='microlog_posts')
    op.drop_table('microlog_posts')
    # ### end Alembic commands ###