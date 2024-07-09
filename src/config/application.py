from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.apps.routers import api_router
from src.config.base import settings


def get_app() -> FastAPI:
    """
    This is the main constructor of an application.
    """
    app = FastAPI(
        title="ERC-20 detector",
        docs_url="/",
        swagger_ui_parameters={
            "displayRequestDuration": True,
            "persistAuthorization": True,
        },
        debug=settings.debug,
    )

    app.include_router(router=api_router, prefix="/api")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=[
            "GET",
            "POST",
            "OPTIONS",
            "DELETE",
            "PATCH",
            "PUT",
        ],
        allow_headers=[
            "Content-Type",
            "Set-Cookie",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin",
            "Authorization",
        ],
    )

    return app
