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
