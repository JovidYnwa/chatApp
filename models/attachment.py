from pydantic import BaseModel


class Attachment(BaseModel):
    attachment_id: str
    message_id: str
    file_name: str
    file_type: str
    file_size: int