from typing import Any

from fastapi import HTTPException, status


class HTTP404Exception(HTTPException):
    def __init__(  # noqa: D107
        self,
        detail: Any = None,
    ) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class HTTP400Exception(HTTPException):
    def __init__(  # noqa: D107
        self,
        detail: Any = None,
    ) -> None:
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
