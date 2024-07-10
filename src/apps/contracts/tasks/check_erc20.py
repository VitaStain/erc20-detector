import logging

from taskiq import TaskiqDepends

from src.apps.contracts.services.contracts import ContractService
from src.apps.contracts.utils.check_source_code import check_source_code
from src.apps.standards.services.standards import StandardService
from src.apps.standards.utils.constants import ContractStatus
from src.config.base import settings
from src.config.tkq import broker
from src.utils.exceptions import HTTP404Exception


@broker.task
async def check_erc20(
    contract_id: int,
    contract_service: ContractService = TaskiqDepends(),
    standard_service: StandardService = TaskiqDepends(),
) -> None:
    """Set standard the contract with contract id"""
    try:
        contract = await contract_service.get_by_id(contract_id)
        await contract_service.edit_one(
            contract_id, {"status": ContractStatus.PROCESSING}
        )
        standards = await standard_service.find_all()
        for standard in standards:
            is_standard = check_source_code(
                [function.name for function in standard.functions],
                contract.source_code,
            )
            if is_standard:
                is_erc20 = (
                    True if standard.name == settings.erc20_standard_name else False
                )
                await contract_service.edit_one(
                    contract_id, {"is_erc20": is_erc20, "standard_id": standard.id}
                )
        await contract_service.edit_one(
            contract_id, {"status": ContractStatus.PROCESSED}
        )
    except HTTP404Exception:
        logging.info(f"Contact with {contract_id=} not found")
    except Exception as e:
        logging.info(f"Contact with {contract_id=} ends checking with exception: {e}")
        await contract_service.edit_one(contract_id, {"status": ContractStatus.FAILED})


@broker.task
async def start_checking_erc20(
    contract_service: ContractService = TaskiqDepends(),
) -> None:
    """Find not checked contracts and start task for set standard"""
    contracts = await contract_service.find_not_checked_contracts()
    for contract in contracts:
        await check_erc20.kiq(contract.id)
