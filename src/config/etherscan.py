from pydantic import BaseModel


class EtherscanSettings(BaseModel):
    url: str = "https://api.etherscan.io/api"
    api_key: str
