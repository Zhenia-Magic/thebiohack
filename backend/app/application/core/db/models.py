from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from application.core.db.database import Base


class DBModel:

    def create(self, db_session):
        db_session.add(self)
        db_session.commit()


class TagPost(Base, DBModel):
    __tablename__ = "tags_posts"

    tag_id = Column(Integer, ForeignKey("tags.tag_id"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.post_id"), primary_key=True)


class Post(Base, DBModel):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    title = Column(String, nullable=False)
    html_content = Column(Text, nullable=False)
    created_at = Column(DateTime)
    in_course = Column(Boolean, nullable=False, index=True)
    order_in_course = Column(Integer, unique=True)

    tags = relationship(
      "Tag", secondary="tags_posts", back_populates="posts"
    )
    questions = relationship("Question", backref="posts")


class Tag(Base, DBModel):
    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    posts = relationship(
      "Post", secondary="tags_posts", back_populates="tags"
    )


class ChallengeUser(Base, DBModel):
    __tablename__ = "challenges_users"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    challenge_id = Column(Integer, ForeignKey("challenges.challenge_id"), primary_key=True)
    days_completed = Column(Integer, nullable=False)
    completed = Column(Boolean, nullable=False)
    ongoing = Column(Boolean, nullable=False)


class Challenge(Base, DBModel):
    __tablename__ = "challenges"

    challenge_id = Column(Integer, primary_key=True, nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.tag_id"), index=True)
    name = Column(String, nullable=False)
    num_days = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)

    users = relationship(
      "User", secondary="challenges_users", back_populates="challenges"
    )


class Question(Base, DBModel):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.post_id"), index=True, nullable=False)
    name = Column(String, nullable=False)
    prompt = Column(Text, nullable=False)

    choices = relationship("QuestionChoice", backref="questions")


class QuestionChoice(Base, DBModel):
    __tablename__ = "question_choices"

    question_choice_id = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.question_id"), index=True, nullable=False)
    text = Column(String, nullable=False)
    correct = Column(Boolean, nullable=False)
    explanation = Column(Text)


class User(Base, DBModel):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    about_me = Column(Text)
    admin = Column(Boolean, index=True, default=False, nullable=False)
    posts = relationship("Post", backref="users")

    challenges = relationship(
      "Challenge", secondary="challenges_users", back_populates="users"
    )

