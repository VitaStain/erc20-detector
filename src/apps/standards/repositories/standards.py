from src.apps.standards.models.standards import Standard
from src.utils.base_repository import SQLAlchemyRepository


class StandardRepository(SQLAlchemyRepository):
    model = Standard
