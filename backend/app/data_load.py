import markdown
from typing import List, Optional, Union
import frontmatter
from sqlalchemy.orm import Session
import os

from application.core.schema.schemas import PostModel, QuestionModel, QuestionChoiceModel, TagModel
from application.core.db.models import Tag, Post, Question, QuestionChoice, User
from application.core.db.database import engine
import json


class PreparedData:

    def __init__(self, posts: Optional[List[Union[PostModel, List[TagModel], list]]],
                 tags: Optional[List[List[str]]]):
        self.posts = posts
        self.tags = tags


def prepare_data(articles_directory: str = '/app/application/data/articles',
                 questions_directory: str = '/app/application/data/questions',
                 tags_json_file: str = '/app/application/data/tags.json',
                 question_choices_directory: str = '/app/application/data/question_choices'):
    with open(tags_json_file) as tags_json:
        tags = json.load(tags_json)['tags']

    tag_names_with_index = {tag: index for index, tag in enumerate(tags)}

    posts = []
    for filename in os.listdir(articles_directory):
        f_post = os.path.join(articles_directory, filename)
        f_questions = os.path.join(questions_directory, filename[:-3] + '.json')
        f_questions_choices = os.path.join(question_choices_directory, filename[:-3] + '.json')
        if os.path.isfile(f_post):
            file = frontmatter.load(f_post)
            post = PostModel(title=file.metadata['title'],
                             created_at=file.metadata['created_at'],
                             in_course=file.metadata['in_course'],
                             order_in_course=file.metadata.get('order_in_course'),
                             html_content=markdown.markdown(file.content))

            post_tags = []
            for tag in file.metadata['tags']:
                tag_ind = tag_names_with_index.get(tag)
                if tag_ind is not None:
                    post_tags.append(TagModel(name=tags[tag_ind]))
                else:
                    tags.append(tag)
                    tag_names_with_index[tag] = len(tags) - 1
                    tag_ind = tag_names_with_index.get(tag)
                    post_tags.append(TagModel(name=tags[tag_ind]))

            post_questions = []
            if os.path.isfile(f_questions):
                with open(f_questions) as questions_json:
                    questions = json.load(questions_json)['questions']
                with open(f_questions_choices) as questions_choices_json:
                    questions_choices = json.load(questions_choices_json)['questions_choices']
                for question, question_choices in zip(questions, questions_choices):
                    question = QuestionModel(**question, post=post)
                    question_choices = [QuestionChoiceModel(**choice, question=question)
                                        for choice in question_choices]
                    post_questions.append([question, question_choices])
            posts.append([post, post_tags, post_questions])
    return PreparedData(tags=tags, posts=posts)


def upload_data(data_for_upload: PreparedData):
    with Session(engine) as session:
        user_exists = session.query(User).filter(User.username == 'evcode').first()
        if not user_exists:
            user = User(username='evcode', hashed_password='$2b$12$gkXl6m2Pv36FHCn3Ptsv5.uVWqUKkHS2Od6uU/m.urbZQj5GOWRB.',
                        email='evgeniiabarabash@gmail.com', first_name='Evgeniia', last_name='Buzulukova',
                        about_me='IT girl from north', admin=True)
            session.add(user)
            session.commit()
            user_exists = session.query(User).filter(User.username == user.username).first()

    for tag in data_for_upload.tags:
        with Session(engine) as session:
            if not session.query(Tag).filter(Tag.name == tag).first():
                session.merge(Tag(name=tag))
                session.commit()

    for post_data in data_for_upload.posts:
        post, post_tags, post_questions = post_data
        with Session(engine) as session:
            post_exists = session.query(Post).filter(Post.title == post.title).first()
            if post_exists:
                post_exists.title = post.title
                post_exists.html_content = post.html_content
                post_exists.user_id = user_exists.user_id
                post_exists.created_at = post.created_at
                post_exists.in_course = post.in_course
                post_exists.order_in_course = post.order_in_course
                post_id = post_exists.post_id
                session.commit()
            else:
                post_dict = post.dict()
                del post_dict['user']
                post_record = Post(**post_dict, user_id=user_exists.user_id)
                post_tags_names = [tag.name for tag in post_tags]
                post_record.tags = session.query(Tag).filter(Tag.name.in_(post_tags_names)).all()
                session.add(post_record)
                session.commit()
                post_exists = session.query(Post).filter(Post.title == post.title).first()
                post_id = post_exists.post_id

            for question, question_choices in post_questions:
                question_exists = session.query(Question).filter(Question.name == question.name,
                                                                 Question.post_id == post_id).first()
                if question_exists:
                    question_exists.name = question.name
                    question_exists.prompt = question.prompt
                    question_id = question_exists.question_id
                else:
                    question_dict = question.dict()
                    del question_dict['post']
                    question_record = Question(**question_dict, post_id=post_id)
                    session.add(question_record)
                    session.commit()
                    question_exists = session.query(Question).filter(Question.name == question.name,
                                                                     Question.post_id == post_id).first()
                    question_id = question_exists.question_id
                    question_exists.choices = []

                for question_choice in question_choices:
                    choice_exists = session.query(QuestionChoice).filter(QuestionChoice.text == question_choice.text,
                                                                         QuestionChoice.question_id == question_id
                                                                         ).first()
                    if choice_exists:
                        choice_exists.text = question_choice.text
                        choice_exists.correct = question_choice.correct
                        choice_exists.explanation = question_choice.explanation
                    else:
                        choice_dict = question_choice.dict()
                        del choice_dict['question']
                        choice_record = QuestionChoice(**choice_dict, question_id=question_id)
                        session.add(choice_record)
                        question_exists.choices.append(choice_record)

            session.commit()


data = prepare_data()
upload_data(data_for_upload=data)

