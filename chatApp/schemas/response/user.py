from pydantic import BaseModel

class UserOut(BaseModel):
    msisdn: str
    login: str

    # def __init__(self):
    #     return self.msisdn
