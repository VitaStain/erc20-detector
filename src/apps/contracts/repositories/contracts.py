from src.apps.contracts.models.contracts import Contract
from src.utils.base_repository import SQLAlchemyRepository
from src.utils.exceptions import HTTP400Exception


class ContractRepository(SQLAlchemyRepository):
    model = Contract

    async def validate_is_exist(self, contract_address: str):
        """Check if contract with this address already exists"""
        if await self.find_one(contract_address=contract_address):
            msg = f"Contract '{contract_address}' already exists"
            raise HTTP400Exception(msg)
