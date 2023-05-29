from pydantic import BaseModel

class User(BaseModel):
    msisdn: str
    login: str

    # def __init__(self):
    #     return self.msisdn
