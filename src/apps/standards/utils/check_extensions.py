import logging
import re
from typing import List

import httpx

from src.apps.standards.models.extensions import Extension
from src.apps.standards.schemas.extensions import ExtensionsSchema, ExceptionParseSchema
from src.apps.standards.schemas.functions import FunctionSchema
from src.apps.standards.services.extensions import ExtensionService


async def get_directory_contents(
    repo_owner: str,
    repo_name: str,
    path: str,
) -> List[dict]:
    """Get list files from github repository"""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            logging.error(f"Error during getting directory contents: {e}")
        return []


async def get_file_contents(
    repo_owner: str,
    repo_name: str,
    path: str,
) -> str:
    """Get code file from github repository"""
    url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/master/{path}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            logging.error(f"Error during getting file contents: {e}")


def extract_functions_and_events(code: str) -> List[str]:
    """Find functions and events in code"""
    elements = re.compile(r"\b(?:function|event)\s+([a-zA-Z_]\w*)\s*\(")
    functions = elements.findall(code)
    return functions


async def process_files(
    repo_owner: str,
    repo_name: str,
    directory: str,
    standard_name: str,
) -> List[ExtensionsSchema]:
    """Parse github repository and create schemas extensions"""
    contents = await get_directory_contents(repo_owner, repo_name, directory)
    extensions = list()

    for item in contents:
        if item["type"] == "file" and item["name"].endswith(".sol"):
            file_contents = await get_file_contents(repo_owner, repo_name, item["path"])
            functions = extract_functions_and_events(file_contents)
            extensions.append(
                ExtensionsSchema(
                    name=item["name"].split(".sol")[0],
                    standard_name=standard_name,
                    functions=[
                        FunctionSchema(name=function_name)
                        for function_name in functions
                    ],
                )
            )
    return extensions


async def check_extensions(
    exception_parce: ExceptionParseSchema,
    extension_service: ExtensionService,
) -> List[Extension]:
    """Start checking extension from github repository"""
    extensions = await process_files(
        exception_parce.repo_owner,
        exception_parce.repo_name,
        exception_parce.directory,
        exception_parce.standard_name,
    )
    list_extensions = []
    for extension in extensions:
        extension = await extension_service.add_one(extension)
        list_extensions.append(extension)
    return list_extensions
