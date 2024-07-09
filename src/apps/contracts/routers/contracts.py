from typing import List

from fastapi import APIRouter, Depends

from src.apps.contracts.schemas.contracts import ContractAddressSchema, ContractSchema
from src.apps.contracts.services.contracts import ContractService

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
