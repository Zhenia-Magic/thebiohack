from typing import List

from fastapi import Depends, APIRouter

from app.core.db.database import get_db
from app.core.db.db_api_utils import create_tag, get_all_tags
from app.core.schema.schemas import TagModel

router = APIRouter()


@router.post("/tag")
async def add_tag(tag: TagModel, db_session=Depends(get_db)):
    create_tag(db_session, tag)


@router.get("/tags", response_model=List[TagModel])
async def get_tags(db_session=Depends(get_db)) -> List[TagModel]:
    return get_all_tags(db_session)
