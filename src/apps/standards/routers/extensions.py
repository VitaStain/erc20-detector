from typing import List

from fastapi import APIRouter, Depends

from src.apps.standards.schemas.extensions import (
    ExtensionsNameSchema,
    ExceptionParseSchema,
)
from src.apps.standards.services.extensions import ExtensionService
from src.apps.standards.utils.check_extensions import check_extensions

router = APIRouter()


@router.post(
    "/",
    response_model=List[ExtensionsNameSchema],
    name="set_extensions",
)
async def set_extensions(
    exception_parce: ExceptionParseSchema,
    extension_service: ExtensionService = Depends(),
):
    return await check_extensions(exception_parce, extension_service)
