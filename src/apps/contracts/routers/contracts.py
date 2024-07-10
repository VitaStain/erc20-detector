from typing import List

from fastapi import APIRouter, Depends

from src.apps.contracts.schemas.contracts import ContractAddressSchema, ContractSchema
from src.apps.contracts.services.contracts import ContractService
from src.apps.contracts.tasks.check_erc20 import start_checking_erc20, check_erc20

router = APIRouter()


@router.post(
    "/",
    response_model=ContractSchema,
    name="add_contract",
)
async def add_contact(
    contract: ContractAddressSchema,
    contract_service: ContractService = Depends(),
):
    return await contract_service.add_one(contract)


@router.get(
    "/{id}",
    response_model=ContractSchema,
    name="get_contract",
)
async def get_contact(
    contract_id: int,
    contract_service: ContractService = Depends(),
):
    return await contract_service.get_by_id(contract_id)


@router.get(
    "/",
    response_model=List[ContractSchema],
    name="get_contracts",
)
async def get_contacts(
    contract_service: ContractService = Depends(),
):
    return await contract_service.find_all()


@router.post(
    "/check_contracts",
    name="check_contracts",
)
async def check_contracts() -> str:
    await start_checking_erc20.kiq()
    return "Start processing"


@router.post(
    "/check_contracts/{contract_id}",
    name="check_contract",
)
async def check_contract(contract_id: int) -> str:
    await check_erc20.kiq(contract_id)
    return "Start processing"
