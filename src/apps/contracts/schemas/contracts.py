from pydantic import BaseModel, Field


class ContractAddressSchema(BaseModel):
    contract_address: str = Field(max_length=50)


class ContractSchema(BaseModel):
    id: int
    contract_address: str = Field(max_length=50)
    source_code: str
    is_erc20: bool | None
    erc20_version: str | None = Field(max_length=50)
    status: str
