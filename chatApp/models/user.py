from pydantic import BaseModel

class User(BaseModel):
    msisdn: str
    login: int

    # def __init__(self):
    #     return self.msisdn
