from pydantic import BaseModel


class CreateMember(BaseModel):
    email: str
    name: str
