from .health_check import health_router
from .v1.item import item_router

routers = [health_router, item_router]
