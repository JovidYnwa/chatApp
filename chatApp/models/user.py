from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

    def __init__(self):
        return self.name
