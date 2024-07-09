from src.apps.standards.schemas.standards import StandardSchema
from src.utils.dependencies.unit_of_work import UOWDep


class StandardService:
    def __init__(self, uow: UOWDep):
        self.uow = uow

    async def add_one(
        self,
        standard_schema: StandardSchema,
    ):
        async with self.uow:
            await self.uow.standards.validate_is_exist(standard_schema.name)
            standard = await self.uow.standards.add_one(
                data={"name": standard_schema.name}
            )
            functions = await self.uow.functions.add_many(
                data=[{"name": function.name} for function in standard_schema.functions]
            )
            await self.uow.function__standard.add_many(
                data=[
                    {"standard_id": standard.id, "function_id": function.id}
                    for function in functions
                ]
            )
            return standard
