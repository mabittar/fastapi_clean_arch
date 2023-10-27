
from fastapi import APIRouter, status

health_router = APIRouter(tags=["healthcheck"])

@health_router.get(
    "/health",
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
async def get_health():
    return {"status": "OK"}
