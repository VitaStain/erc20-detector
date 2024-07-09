from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.apps.standards.models.standards import (
    Standard,
    FunctionStandardSecondary,
)
from src.utils.base_repository import SQLAlchemyRepository
from src.utils.exceptions import HTTP400Exception, HTTP404Exception


class StandardRepository(SQLAlchemyRepository):
    model = Standard

    async def validate_is_exist(self, name: str):
        if await self.find_one(name=name):
            msg = f"Standard '{name}' already exists"
            raise HTTP400Exception(msg)

    async def get_by_name(self, name: str):
        stmt = (
            select(self.model)
            .options(joinedload(self.model.functions))
            .filter_by(name=name)
        )
        res = await self.session.execute(stmt)
        res = res.scalar()
        if not res:
            msg = f"Standard doesn't exist"
            raise HTTP404Exception(msg)
        return res

    async def find_all(self, **filter_by):
        stmt = (
            select(self.model)
            .options(joinedload(self.model.functions))
            .filter_by(**filter_by)
        )
        res = await self.session.execute(stmt)
        res = res.scalars().unique().all()
        return res


class FunctionStandardSecondaryRepository(SQLAlchemyRepository):
    model = FunctionStandardSecondary
