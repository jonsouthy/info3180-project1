"""empty message

Revision ID: 9c599509aa29
Revises: 
Create Date: 2018-03-18 19:10:39.041336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c599509aa29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=80), nullable=True),
    sa.Column('lname', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('userid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###