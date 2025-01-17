from typing import Annotated

from fastapi import Depends

from src.utils.unit_of_work import UnitOfWork, IUnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
