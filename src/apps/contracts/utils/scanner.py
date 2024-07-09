import logging

import httpx

from src.apps.contracts.utils.constants import Modules, Parameters, Actions
from src.config.base import settings


class Scanner:

    @staticmethod
    def get_url_for_get_contract_code(address: str) -> str:
        """Build url for getting contract source code"""
        url = (
            f"{settings.etherscan.url}"
            f"?{Parameters.MODULE}={Modules.CONTRACT}"
            f"&{Parameters.ACTION}={Actions.GETSOURCECODE}"
            f"&{Parameters.ADDRESS}={address}"
            f"&{Parameters.APIKEY}={settings.etherscan.api_key}"
        )
        return url

    async def get_contract_code(self, url: str) -> str | None:
        """Get contract source code from url"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                data = response.json()
                if data["status"] == "1" and data["message"] == "OK":
                    return data["result"][0]["SourceCode"]
            except Exception as e:
                logging.info(f"Exception during getting source code contract: {e}")


scanner = Scanner()
