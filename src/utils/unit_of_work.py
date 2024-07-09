from abc import ABC, abstractmethod
from typing import Type

from fastapi import Depends

from src.apps.contracts.repositories.contracts import ContractRepository
from src.apps.standards.repositories.functions import FunctionRepository
from src.apps.standards.repositories.standards import StandardRepository
from src.utils.dependencies.get_db_session import get_db_session


class IUnitOfWork(ABC):
    # contracts
    contract: Type[ContractRepository]
    # standards
    functions = Type[FunctionRepository]
    standards = Type[StandardRepository]

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    async def __aexit__(self, exn_type, exn_value, traceback):
        if exn_type is None:
            await self.commit()
        else:
            await self.rollback()

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork(IUnitOfWork):
    def __init__(self, db_session=Depends(get_db_session)):
        self.session = db_session

    async def __aenter__(self):
        # contracts
        self.accounts = ContractRepository(self.session)
        # standards
        self.functions = FunctionRepository(self.session)
        self.standards = StandardRepository(self.session)
        return self

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
