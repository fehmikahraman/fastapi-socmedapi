from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
   

    comments = relationship("Comment", back_populates="owner")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    owner = relationship("Post", back_populates="comments")
