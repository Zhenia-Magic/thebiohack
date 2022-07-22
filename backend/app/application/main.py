from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from application.core.config import settings
from application.core.db.admin_models import UserAdmin, TagAdmin, PostAdmin, QuestionAdmin, QuestionChoiceAdmin, \
  ChallengeAdmin
from application.core.db.database import engine
from application.routes.api import api_router


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
admin = Admin(app, engine)

for admin_model in [UserAdmin, TagAdmin, PostAdmin, QuestionAdmin, QuestionChoiceAdmin,
                    ChallengeAdmin]:
    admin.register_model(admin_model)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router)
