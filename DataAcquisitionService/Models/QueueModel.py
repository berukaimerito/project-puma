from pydantic import BaseModel, Field

class Queue(BaseModel):
    user_name: str = Field(...)
    symbol: str = Field(...)
