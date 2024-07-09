from src.apps.contracts.schemas.contracts import ContractAddressSchema
from src.apps.contracts.utils.scanner import scanner
from src.utils.dependencies.unit_of_work import UOWDep
from src.utils.exceptions import HTTP400Exception


class ContractService:
    def __init__(self, uow: UOWDep):
        self.uow = uow

    async def add_one(
        self,
        contract: ContractAddressSchema,
    ):
        """Add contract data to database"""
        url = scanner.get_url_for_get_contract_code(contract.contract_address)
        source_code = await scanner.get_contract_code(url)
        if not source_code:
            msg = f"Error during getting source code contract"
            raise HTTP400Exception(msg)
        async with self.uow:
            contract = await self.uow.contracts.add_one(
                data={
                    "contract_address": contract.contract_address,
                    "source_code": source_code,
                }
            )

        return contract
