from fastapi.routing import APIRouter

from src.apps.contracts.routers.contracts import router as contract_routers
from src.apps.standards.routers.standards import router as standard_routers

api_router = APIRouter(prefix="/v1")
# standards
api_router.include_router(
    standard_routers,
    prefix="/standards",
    tags=["standards"],
)
# contracts
api_router.include_router(
    contract_routers,
    prefix="/contracts",
    tags=["contracts"],
)
