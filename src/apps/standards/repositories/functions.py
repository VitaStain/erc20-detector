from src.apps.standards.models.functions import Function
from src.utils.base_repository import SQLAlchemyRepository


class FunctionRepository(SQLAlchemyRepository):
    model = Function
