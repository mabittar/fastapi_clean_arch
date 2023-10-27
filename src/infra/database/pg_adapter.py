from typing import Annotated, AsyncIterator

from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import settings

Base = declarative_base()

# Realiza a conexão com o banco de dados
async_engine = create_async_engine(
    settings.DATABASE_URI,
    echo=False,
    future=True,
)

AsyncSessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def async_get_db() -> AsyncSession:
    try:
        yield AsyncSessionLocal
    except SQLAlchemyError as e:
        raise e
    # async_session = local_session()
    # try:
    #     yield async_session
    #     await async_session.commit()
    # except SQLAlchemyError:
    #     await async_session.rollback()
    #     raise
    # finally:
    #     await async_session.close()
    # async with async_session() as db:
    #     yield db
    #     await db.commit()


AsyncSessionDI = Annotated[sessionmaker, Depends(async_get_db)]
