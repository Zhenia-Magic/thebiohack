import pytest
from sqlalchemy.orm import Session

from app.core.db.db_api_utils import get_all_posts, get_posts_by_tag
from app.core.db.models import Tag, Post, TagPost
from app.core.schema.schemas import TagModel
from test.test_utils import db_session, db_engine


def add_posts(db_session: Session):
    post1 = Post(post_id=1, title="Post_1", html_content="hello world", in_course=False)
    post2 = Post(post_id=2, title="Post_1", html_content="hello world", in_course=False)
    post3 = Post(post_id=3, title="Post_1", html_content="hello world", in_course=False)
    for post in [post1, post2, post3]:
        db_session.add(post)
        db_session.add(TagPost(post_id=post.post_id, tag_id=1))
    db_session.commit()


def test_tags(db_session: Session):
    assert [TagModel(**vars(tag)).name for tag in db_session.query(Tag).all()] == ['Sleep', 'Nutrition',
                                                                                   'Exercise', 'Work', 'Brain']


def test_add_post(db_session: Session):
    add_posts(db_session)
    assert len(get_all_posts(db_session)) == 3
    assert len(get_posts_by_tag(db_session, 1)) == 3


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, '-v', '--import-mode=importlib']))
