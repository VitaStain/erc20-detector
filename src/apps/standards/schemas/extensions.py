from typing import List

from pydantic import BaseModel

from src.apps.standards.schemas.functions import FunctionSchema
from src.config.base import settings


class ExtensionsSchema(BaseModel):
    name: str
    functions: List[FunctionSchema]
    standard_name: str


class ExtensionsNameSchema(BaseModel):
    id: int
    name: str


class ExceptionParseSchema(BaseModel):
    repo_owner: str = settings.extensions_repo_owner
    repo_name: str = settings.extensions_repo_name
    directory: str = settings.extensions_directory
    standard_name: str = "ERC-20"
