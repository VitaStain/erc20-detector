from fastapi import APIRouter, Depends

from src.apps.standards.schemas.standards import StandardSchema, StandardNameSchema
from src.apps.standards.services.standards import StandardService

router = APIRouter()


@router.post(
    "/",
    response_model=StandardNameSchema,
    name="add_standards",
)
async def add_standards(
    standards: StandardSchema,
    standard_service: StandardService = Depends(),
):
    return await standard_service.add_one(standards)
