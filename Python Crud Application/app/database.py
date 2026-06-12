from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
class Base(DeclarativeBase):
    """"DeclarativeBase"""

engine = create_async_engine(
    settings.DATABASE_URL,
    echo= settings.DB_ECHO,
    pool_size = 5,
    pool_overflow = 30,
    pool_recycle = 1800,
    pool_pre_ping = True
)

async_session = async_sessionmaker(
    bind = engine,
    class_=AsyncSession,
    autoflush= True,
    expire_on_commit= False
)

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session = async_session()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()

async def init_db() -> None:
    from app import models 
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

async def kill_engine() -> None:
    await engine.dispose()
