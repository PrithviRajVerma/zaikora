from datetime import datetime, timezone
from fastapi import APIRouter
from app.core.config import settings
from app.schemas.health import HealthResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check endpoint",
    description="Check the operational status of the Zaikora API.",
)
async def check_health() -> HealthResponse:
    return HealthResponse(
        success=True,
        message="Zaikora API is running successfully.",
        environment=settings.NODE_ENV,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
