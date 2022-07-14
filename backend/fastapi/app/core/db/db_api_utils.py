from typing import List

from sqlalchemy.orm import Session

from app.core.db.models import User, Tag, Post, Question, Challenge
from app.core.schema.schemas import TagModel, PostModel, QuestionModel, ChallengeModel, QuestionChoiceModel, UserModel


def get_posts_written_by_user(db_session: Session, user_id: int) -> List[PostModel]:
    return [PostModel(**vars(post)) for post in db_session.query(User).filter_by(user_id=user_id).first().posts]


def get_posts_by_tag(db_session: Session, tag_id: int) -> List[PostModel]:
    return [PostModel(**vars(post)) for post in db_session.query(Tag).filter_by(tag_id=tag_id).first().posts]


def get_post_tags(db_session: Session, post_id: int) -> List[TagModel]:
    return [TagModel(**vars(tag)) for tag in db_session.query(Post).filter_by(post_id=post_id).first().tags]


def get_questions_for_post(db_session: Session, post_id: int) -> List[QuestionModel]:
    return [QuestionModel(**vars(question)) for question in
            db_session.query(Post).filter_by(post_id=post_id).first().questions]


def get_question_choices_for_question(db_session: Session, question_id: int) -> List[QuestionChoiceModel]:
    return [QuestionChoiceModel(**vars(choice)) for choice in
            db_session.query(Question).filter_by(question_id=question_id).first().choices]


def get_users_in_challenge(db_session: Session, challenge_id: int) -> List[UserModel]:
    return [UserModel(**vars(user)) for user in
            db_session.query(Challenge).filter_by(challenge_id=challenge_id).first().users]


def get_user_challenges(db_session: Session, user_id: int) -> List[UserModel]:
    return [Challenge(**vars(challenge)) for challenge in
            db_session.query(User).filter_by(user_id=user_id).first().challenges]


def get_all_posts(db_session: Session) -> List[PostModel]:
    return [PostModel(**vars(post)) for post in db_session.query(Post).all()]


def get_all_tags(db_session: Session) -> List[TagModel]:
    return [TagModel(**vars(tag)) for tag in db_session.query(Tag).all()]


def get_all_challenges(db_session: Session) -> List[ChallengeModel]:
    return [ChallengeModel(**vars(challenge)) for challenge in db_session.query(Challenge).all()]


def create_tag(db_session: Session, tag: TagModel) -> List[PostModel]:
    return Tag(**vars(tag)).create(db_session)
