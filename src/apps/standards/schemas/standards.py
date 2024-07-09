from typing import List

from pydantic import BaseModel, Field

from src.apps.standards.schemas.functions import FunctionSchema


class StandardSchema(BaseModel):
    name: str = Field(max_length=100)
    functions: List[FunctionSchema]


class StandardNameSchema(BaseModel):
    name: str = Field(max_length=100)
