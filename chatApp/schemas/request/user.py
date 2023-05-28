from pydantic import BaseModel, Field
from typing import List


class UserContactsIn(BaseModel):
    msisdns: List[str]