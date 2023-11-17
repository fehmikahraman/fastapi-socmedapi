from fastapi import APIRouter, HTTPException, Depends
from socmedapi.models.post import CommentIn
from sqlalchemy.orm import Session
from socmedapi.database.database import SessionLocal
from socmedapi.database import crud, schemas

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/post", response_model=schemas.UserPost, status_code=201)
async def create_post(post: schemas.UserPostIn, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)


@router.get("/posts", response_model=list[schemas.UserPost])
async def get_all_posts(skip: int= 0, limit= 100, db: Session= Depends(get_db)):
    posts = crud.get_posts(db, skip= skip, limit= limit)
    return posts


@router.post("/comment", response_model=schemas.Comment, status_code=201)
async def create_comment_for_post(comment: CommentIn, db: Session= Depends(get_db)):
    post_commented = crud.get_post (db, post_id = comment.post_id)
    if not post_commented:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.create_post_comment(db=db, comment=comment)
   


@router.get("/post/{post_id}/comment", response_model=list[schemas.Comment])
async def get_comments_on_post(post_id: int, db: Session= Depends(get_db) ):
    return crud.get_comments_with_post_id(db=db, post_id=post_id)
    

@router.get("/post/{post_id}", response_model=schemas.UserPost)
async def get_post_with_comments(post_id: int, db: Session= Depends(get_db)):
    post = crud.get_post(db, post_id= post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post