from abc import ABC, abstractmethod
from typing import TypeVar, Type, List, Sequence
from uuid import UUID

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, *args, **kwargs):
        raise NotImplementedError


T = TypeVar("T")


class SQLAlchemyRepository(AbstractRepository):
    model: Type[T] = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> Type[T]:
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def add_many(self, data: list[dict]) -> Sequence[T]:
        stmt = insert(self.model).values(data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def edit_one(self, id: int, data: dict) -> Type[T]:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def edit_many(self, id: List[int], data: dict) -> Sequence[int]:
        stmt = (
            update(self.model)
            .values(**data)
            .where(self.model.id.in_(id))
            .returning(self.model.id)
        )
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar()
        return res

    async def find_all(self, **filter_by) -> Sequence[T]:
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def delete_many(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by).returning(self.model)
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return res

    async def get_by_id(self, id: int | UUID) -> Type[T]:
        stmt = select(self.model).filter(self.model.id == id)
        res = await self.session.execute(stmt)
        return res.scalars().first()
