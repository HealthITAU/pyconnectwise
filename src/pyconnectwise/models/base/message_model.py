from pydantic import BaseModel

class GenericMessageModel(BaseModel):
    message: str