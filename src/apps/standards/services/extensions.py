from typing import Sequence

from src.apps.standards.models.extensions import Extension
from src.apps.standards.schemas.extensions import ExtensionsSchema
from src.utils.dependencies.unit_of_work import UOWDep


class ExtensionService:
    def __init__(self, uow: UOWDep):
        self.uow = uow

    async def add_one(
        self,
        extension_schema: ExtensionsSchema,
    ) -> Extension:
        """Add extension to database"""
        async with self.uow:
            extension = await self.uow.extensions.get_by_name(extension_schema.name)
            if not extension:
                functions = await self.uow.functions.add_many(
                    data=[
                        {"name": function.name}
                        for function in extension_schema.functions
                    ]
                )
                standard = await self.uow.standards.get_by_name(
                    name=extension_schema.standard_name
                )
                extension = await self.uow.extensions.add_one(
                    data={"name": extension_schema.name, "standard_id": standard.id}
                )
                await self.uow.function__extension.add_many(
                    data=[
                        {"extension_id": extension.id, "function_id": function.id}
                        for function in functions
                    ]
                )
            return extension

    async def find_all(self, standard_id: int) -> Sequence[Extension]:
        """Find all extensions from database"""
        async with self.uow:
            return await self.uow.extensions.find_all(standard_id=standard_id)
