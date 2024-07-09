import uvicorn

from src.config.base import settings


def main():
    uvicorn.run(
        "src.config.application:get_app",
        reload=settings.reload,
        host=settings.host,
        port=settings.port,
        workers=settings.workers_count,
    )


if __name__ == "__main__":
    main()
