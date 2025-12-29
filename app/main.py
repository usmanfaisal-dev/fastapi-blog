from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import blog,user , authentication

app = FastAPI(
    title="FastAPI Blog API",
    version="1.0.0"
)

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

