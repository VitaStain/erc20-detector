from src.apps.standards.models.standards import (
    Standard,
    FunctionStandardSecondary,
)
from src.utils.base_repository import SQLAlchemyRepository
from src.utils.exceptions import HTTP400Exception


class StandardRepository(SQLAlchemyRepository):
    model = Standard

    async def validate_is_exist(self, name: str):
        if await self.find_one(name=name):
            msg = f"Standard '{name}' already exists"
            raise HTTP400Exception(msg)


class FunctionStandardSecondaryRepository(SQLAlchemyRepository):
    model = FunctionStandardSecondary
