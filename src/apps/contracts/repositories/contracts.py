from src.apps.contracts.models.contracts import Contract
from src.utils.base_repository import SQLAlchemyRepository


class ContractRepository(SQLAlchemyRepository):
    model = Contract
