"""init

Revision ID: 7ed5d67e4abd
Revises: 
Create Date: 2023-09-07 22:32:32.478256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ed5d67e4abd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bank_account',
    sa.Column('balance', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bank_account'))
    )
    op.create_table('bank_customer',
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('bank_account_id', sa.Uuid(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['bank_account_id'], ['bank_account.id'], name=op.f('fk_bank_customer_bank_account_id_bank_account')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bank_customer')),
    sa.UniqueConstraint('first_name', 'last_name', name=op.f('uq_bank_customer_first_name_last_name')),
    sa.UniqueConstraint('id', 'bank_account_id', name=op.f('uq_bank_customer_id_bank_account_id'))
    )
    op.create_table('bank_operation',
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('bank_account_id', sa.Uuid(), nullable=False),
    sa.Column('bank_customer_id', sa.Uuid(), nullable=False),
    sa.Column('bank_operation_type', sa.Enum('DEPOSIT', 'WITHDRAW', name='bankoperationsdb'), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['bank_account_id'], ['bank_account.id'], name=op.f('fk_bank_operation_bank_account_id_bank_account')),
    sa.ForeignKeyConstraint(['bank_customer_id'], ['bank_customer.id'], name=op.f('fk_bank_operation_bank_customer_id_bank_customer')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bank_operation'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bank_operation')
    op.drop_table('bank_customer')
    op.drop_table('bank_account')
    # ### end Alembic commands ###