from typing import List

from fastapi import APIRouter, Depends

from src.apps.standards.schemas.standards import StandardSchema, StandardNameSchema
from src.apps.standards.services.standards import StandardService

router = APIRouter()


@router.post(
    "/",
    response_model=StandardNameSchema,
    name="add_standard",
)
async def add_standards(
    standard: StandardSchema,
    standard_service: StandardService = Depends(),
):
    return await standard_service.add_one(standard)


@router.delete(
    "/{standard_name}",
    status_code=204,
    name="delete_standard",
)
async def delete_standard(
    standard_name: str,
    standard_service: StandardService = Depends(),
):
    await standard_service.delete_one(standard_name)


@router.get(
    "/{standard_name}",
    response_model=StandardSchema,
    name="get_standard",
)
async def get_standard(
    standard_name: str,
    standard_service: StandardService = Depends(),
):
    return await standard_service.get_by_name(standard_name)


@router.get(
    "/",
    response_model=List[StandardSchema],
    name="get_standards",
)
async def get_standards(
    standard_service: StandardService = Depends(),
):
    return await standard_service.find_all()
