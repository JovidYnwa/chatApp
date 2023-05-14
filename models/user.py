from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Post(BaseModel):
    name1: str
    desc1: str