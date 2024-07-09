from pydantic import BaseModel, Field


class ContractAddressSchema(BaseModel):
    contract_address: str = Field(max_length=50)
