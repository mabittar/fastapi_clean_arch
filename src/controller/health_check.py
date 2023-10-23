
from fastapi import APIRouter,status


health_router = APIRouter(tags=["health_check"])

@health_router.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
async def get_health():
    return {"status": "OK"}
