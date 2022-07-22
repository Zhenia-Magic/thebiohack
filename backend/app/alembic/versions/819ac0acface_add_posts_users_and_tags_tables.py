"""Add posts, users, and tags tables

Revision ID: 819ac0acface
Revises:
Create Date: 2022-07-08 22:02:21.441590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '819ac0acface'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('tag_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_admin'), 'users', ['admin'], unique=False)
    op.create_table('challenges',
    sa.Column('challenge_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('num_days', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.tag_id'], ),
    sa.PrimaryKeyConstraint('challenge_id')
    )
    op.create_index(op.f('ix_challenges_tag_id'), 'challenges', ['tag_id'], unique=False)
    op.create_table('posts',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('html_content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('in_course', sa.Boolean(), nullable=False),
    sa.Column('order_in_course', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('post_id'),
    sa.UniqueConstraint('order_in_course')
    )
    op.create_index(op.f('ix_posts_in_course'), 'posts', ['in_course'], unique=False)
    op.create_index(op.f('ix_posts_user_id'), 'posts', ['user_id'], unique=False)
    op.create_table('challenges_users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=False),
    sa.Column('days_completed', sa.Integer(), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.Column('ongoing', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenges.challenge_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'challenge_id')
    )
    op.create_table('questions',
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('prompt', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.post_id'], ),
    sa.PrimaryKeyConstraint('question_id')
    )
    op.create_index(op.f('ix_questions_post_id'), 'questions', ['post_id'], unique=False)
    op.create_table('tags_posts',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.post_id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.tag_id'], ),
    sa.PrimaryKeyConstraint('tag_id', 'post_id')
    )
    op.create_table('question_choices',
    sa.Column('question_choice_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('correct', sa.Boolean(), nullable=False),
    sa.Column('explanation', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.question_id'], ),
    sa.PrimaryKeyConstraint('question_choice_id')
    )
    op.create_index(op.f('ix_question_choices_question_id'), 'question_choices', ['question_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_question_choices_question_id'), table_name='question_choices')
    op.drop_table('question_choices')
    op.drop_table('tags_posts')
    op.drop_index(op.f('ix_questions_post_id'), table_name='questions')
    op.drop_table('questions')
    op.drop_table('challenges_users')
    op.drop_index(op.f('ix_posts_user_id'), table_name='posts')
    op.drop_index(op.f('ix_posts_in_course'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_challenges_tag_id'), table_name='challenges')
    op.drop_table('challenges')
    op.drop_index(op.f('ix_users_admin'), table_name='users')
    op.drop_table('users')
    op.drop_table('tags')
    # ### end Alembic commands ###
