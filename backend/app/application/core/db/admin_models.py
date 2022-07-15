from sqladmin import ModelAdmin

from application.core.db.models import User, Tag, Post, Question, Challenge, QuestionChoice


class UserAdmin(ModelAdmin, model=User):
    column_list = [User.user_id, User.username, User.hashed_password, User.email, User.first_name,
                   User.last_name, User.about_me, User.admin]


class TagAdmin(ModelAdmin, model=Tag):
    column_list = [Tag.tag_id, Tag.name]


class PostAdmin(ModelAdmin, model=Post):
    column_list = [Post.post_id, Post.user_id, Post.title, Post.html_content,
                   Post.in_course, Post.order_in_course]


class QuestionAdmin(ModelAdmin, model=Question):
    column_list = [Question.question_id, Question.post_id, Question.name, Question.prompt]


class ChallengeAdmin(ModelAdmin, model=Challenge):
    column_list = [Challenge.challenge_id, Challenge.tag_id, Challenge.name, Challenge.num_days,
                   Challenge.description]


class QuestionChoiceAdmin(ModelAdmin, model=QuestionChoice):
    column_list = [QuestionChoice.question_choice_id, QuestionChoice.question_id,
                   QuestionChoice.text, QuestionChoice.correct,
                   QuestionChoice.explanation]

