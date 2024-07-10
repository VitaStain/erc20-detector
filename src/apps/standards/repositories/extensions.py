from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.apps.standards.models.extensions import Extension, FunctionExtensionSecondary
from src.utils.base_repository import SQLAlchemyRepository


class ExtensionRepository(SQLAlchemyRepository):
    model = Extension

    async def get_by_name(self, name: str):
        """Get extension from database by name with join function model"""
        stmt = select(self.model).filter_by(name=name)
        res = await self.session.execute(stmt)
        res = res.scalar()
        return res

    async def find_all(self, **filter_by):
        """Get all extensions from database with join function model"""
        stmt = (
            select(self.model)
            .options(joinedload(self.model.functions))
            .filter_by(**filter_by)
        )
        res = await self.session.execute(stmt)
        res = res.scalars().unique().all()
        return res


class FunctionExtensionSecondaryRepository(SQLAlchemyRepository):
    model = FunctionExtensionSecondary
