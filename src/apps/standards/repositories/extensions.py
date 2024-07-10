from sqlalchemy import select

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


class FunctionExtensionSecondaryRepository(SQLAlchemyRepository):
    model = FunctionExtensionSecondary
