from src.apps.contracts.schemas.contracts import ContractAddressSchema
from src.apps.contracts.utils.scanner import scanner
from src.utils.dependencies.unit_of_work import UOWDep
from src.utils.exceptions import HTTP400Exception, HTTP404Exception


class ContractService:
    def __init__(self, uow: UOWDep):
        self.uow = uow

    async def add_one(
        self,
        contract: ContractAddressSchema,
    ):
        """Add contract data to database"""

        async with self.uow:
            await self.uow.contracts.validate_is_exist(contract.contract_address)
            url = scanner.get_url_for_get_contract_code(contract.contract_address)
            source_code = await scanner.get_contract_code(url)
            if not source_code:
                msg = f"Error during getting source code contract"
                raise HTTP400Exception(msg)
            contract = await self.uow.contracts.add_one(
                data={
                    "contract_address": contract.contract_address,
                    "source_code": source_code,
                }
            )

        return contract

    async def get_by_id(self, contract_id: int):
        """Get contract by id from database"""
        async with self.uow:
            contract = await self.uow.contracts.get_by_id(contract_id)
            if not contract:
                msg = f"Contract doesn't exist"
                raise HTTP404Exception(msg)
        return contract

    async def find_all(self, **filter_by):
        """Get all contracts from database"""
        async with self.uow:
            res = await self.uow.contracts.find_all(*filter_by)
        return res
