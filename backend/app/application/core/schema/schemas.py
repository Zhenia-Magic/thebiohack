from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserModel(BaseModel):
    user_id: Optional[int]
    username: str
    hashed_password: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    about_me: Optional[str]
    admin: bool

    class Config:
        orm_mode = True


class PostModel(BaseModel):
    post_id: Optional[int]
    user_id: Optional[int]
    title: str
    html_content: str
    created_at: Optional[datetime]
    in_course: bool
    order_in_course: Optional[int]

    class Config:
        orm_mode = True


class TagModel(BaseModel):
    tag_id: Optional[int]
    name: str

    class Config:
        orm_mode = True


class ChallengeModel(BaseModel):
    challenge_id: Optional[int]
    tag_id: Optional[int]
    name: str
    num_days: int
    description: str

    class Config:
        orm_mode = True


class QuestionModel(BaseModel):
    question_id: Optional[int]
    post_id: int
    name: str
    prompt: str

    class Config:
        orm_mode = True


class QuestionChoiceModel(BaseModel):
    question_choice_id: Optional[int]
    question_id: int
    text: str
    correct: bool
    explanation: Optional[str]
