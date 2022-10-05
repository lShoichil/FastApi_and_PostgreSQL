from typing import List
from fastapi import APIRouter, Depends, status
from microblog import schemas, models
from core import database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
