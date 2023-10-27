from fastapi import FastAPI

from src.config import AppSettings, settings
from src.infra.database.pg_adapter import Base, async_engine

from .controller import routers


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def create_application() -> FastAPI:
    if isinstance(settings, AppSettings):
        application = FastAPI(
            title=settings.APP_NAME,
            description=settings.APP_DESCRIPTION,
        )
    else:
        application = FastAPI()

    if routers:
        for route in routers:
            application.include_router(route)

    # criar tabelas
    application.add_event_handler("startup", create_tables)

    return application

# Crie uma instância do FastAPI
app = create_application()


# Inicialização do arquivo Python
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
