from sqlalchemy.orm import Session

from . import models, schemas




def create_post(db: Session, post: schemas.UserPostIn):
    db_post = models.Post(body=post.body)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post (db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_posts (db: Session, skip: int =0, limit: int =100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_post_comment(db: Session, comment: schemas.CommentIn):
    db_comment = models.Comment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_with_post_id (db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id==post_id).all()