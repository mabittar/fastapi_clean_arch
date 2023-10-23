from fastapi import FastAPI

from .controller import routers
# Crie uma instância do FastAPI
app = FastAPI()
if routers:
    for route in routers:
        app.include_router(route)

# Inicialização do arquivo Python
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
