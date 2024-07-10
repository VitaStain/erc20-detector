from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.apps.routers import api_router
from src.config.base import settings
from src.config.tkq import broker


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not broker.is_worker_process:
        await broker.startup()

    yield

    if not broker.is_worker_process:
        await broker.shutdown()


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
        lifespan=lifespan,
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
