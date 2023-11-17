from pydantic import BaseModel

class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int
    class Config:
        orm_mode = True

class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int
    comments: list[Comment] = []
    class Config:
        orm_mode = True




