from pydantic import BaseModel, Field


class FunctionSchema(BaseModel):
    name: str = Field(max_length=100)
