from pydantic import BaseModel, Field

class QueueModel(BaseModel):
    user_name: str = Field(...)
    symbol: str = Field(...)