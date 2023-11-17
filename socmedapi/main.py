from fastapi import FastAPI
from socmedapi.routers.posts import router as posts_router
from socmedapi.database import models
from socmedapi.database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(posts_router)

