from sqlalchemy.ext.asyncio import AsyncSession

from src.config.base import db_helper


async def get_db_session():
    """Dependency for getting async session"""
    try:
        session: AsyncSession = db_helper.get_scoped_session()
        yield session
    finally:
        await session.close()
