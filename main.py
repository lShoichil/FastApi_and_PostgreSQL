from fastapi import FastAPI

from microblog.routers import blog

app = FastAPI()

app.include_router(blog.router)
