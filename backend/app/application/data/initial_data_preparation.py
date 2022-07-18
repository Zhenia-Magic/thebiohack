import markdown
from typing import List, Optional, Union, Dict
import frontmatter
import os
from application.core.schema.schemas import PostModel, QuestionModel, QuestionChoiceModel, TagModel
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

    tag_names_with_index = {tag['name']: index for index, tag in enumerate(tags)}

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
                    post_tags.append(TagModel(**tags[tag_ind]))
                else:
                    tags.append({"tag_id": len(tags) + 1, "name": tag})
                    tag_names_with_index[tag] = len(tags) - 1
                    tag_ind = tag_names_with_index.get(tag)
                    post_tags.append(TagModel(**tags[tag_ind]))

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

prepare_data()
