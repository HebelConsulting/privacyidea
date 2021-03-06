"""Update AuthCache.authentication to VARCHAR(255) to accommodate argon2 hashes.

Revision ID: 8d40dbcfda25
Revises: 140ba0ca4f07
Create Date: 2020-11-02 17:57:12.493515

"""

# revision identifiers, used by Alembic.
revision = '8d40dbcfda25'
down_revision = '140ba0ca4f07'

from alembic import op
import sqlalchemy as sa

def upgrade():
    try:
        # ### commands auto generated by Alembic - please adjust! ###
        op.alter_column('authcache', 'authentication',
                        existing_type=sa.Unicode(length=64),
                        type_=sa.Unicode(length=255),
                        existing_nullable=True)
        # ### end Alembic commands ###
    except Exception as exx:
        print('Modifying of authcache column "authentication" failed: {!r}'.format(exx))
        print('This is expected behavior if the columns have already been modified.')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('authcache', 'authentication',
                    existing_type=sa.Unicode(length=255),
                    type_=sa.Unicode(length=64),
                    existing_nullable=True)
    # ### end Alembic commands ###
