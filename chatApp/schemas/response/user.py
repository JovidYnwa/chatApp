from pydantic import BaseModel

class UserOut(BaseModel):
    msisdn: str
    login: int

    # def __init__(self):
    #     return self.msisdn
