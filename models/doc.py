from pydantic import BaseModel

class Doc(BaseModel):
  title: str
  body: str