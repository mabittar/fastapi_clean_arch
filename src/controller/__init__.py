from .health_check import health_router
from .v1.item_controller import item_router

routers = [health_router, item_router]
